from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.session.passives import Passive


def _has_colress_in_opponent_discard(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    discard = board.find_player_area(opponent, "discard")
    if not discard:
        return False
    for card in discard.children:
        name = getattr(def_for(card.archetype_id), "display_name", "") or ""
        if "Colress" in name:
            return True
    return False


class PlasmaBanePassive(Passive):
    """If the opponent has a Colress card in their discard pile, Trifrost
    costs [C]."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        if not _has_colress_in_opponent_discard(board, pokemon.owning_player_id):
            return cost
        return {"Colorless": 1}


async def trifrost(ctx):
    """Discard all Energy, then 110 to 3 of the opponent's Pokémon."""
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Choose Energy to discard from this Pokémon"
    )
    candidates = ctx.opponent_pokemon_in_play()
    if candidates:
        await snipe_attack(110, pool="any", count=min(3, len(candidates)))(ctx)


card = PokemonCardDef(
    guid="9286fd09-1515-5602-8b39-1657e9119acf",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem","Basic","Kyurem"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    family_id=646,
    retreat_cost=2,
    abilities=[
        Ability(
            title="Plasma Bane",
            game_text="If your opponent has any cards in their discard pile that have \"Colress\" in the name, this Pokémon can use the Trifrost attack for Colorless.",
            passive=PlasmaBanePassive(),
        ),
        Attack(
            title="Trifrost",
            game_text="Discard all Energy from this Pokémon. This attack does 110 damage to 3 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=trifrost,
        ),
    ],
)
