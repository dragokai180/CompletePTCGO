from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.models.board import BoardState
from spirit.game.session.passives import Passive


class AncientBulwarkPassive(Passive):
    """While this Pokémon is on your Bench, prevent all damage done to each
    of your Pokémon by attacks from your opponent's Pokémon that have 2 or
    less Energy attached."""

    def prevents_damage(self, calc, carrier):
        if is_in_active_spot(carrier):
            return False
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target.owning_player_id != carrier.owning_player_id:
            return False
        if calc.attacker is None:
            return False
        return len(BoardState.attached_energies(calc.attacker)) <= 2


card = PokemonCardDef(
    guid="415b1d30-c648-5c86-b84e-00e20262825c",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon","Stage 2","Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    family_id=410,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    abilities=[
        Ability(
            title="Ancient Bulwark",
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to each of your Pokémon by attacks from your opponent's Pokémon that have 2 or less Energy attached.",
            passive=AncientBulwarkPassive(),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
