from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class WonderKissPassive(Passive):
    """When the opponent's Active Pokémon is Knocked Out, flip a coin. If
    heads, take 1 more Prize card. Does not stack."""

    stacking_key = "WonderKiss"

    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return 0
        if not is_in_active_spot(pokemon):
            return 0
        heads = await ctx.flip_coins(1, "Wonder Kiss", source=carrier)
        return 1 if heads and heads[0] else 0


card = PokemonCardDef(
    guid="3663b0f7-0cc2-57e1-b276-5091ba1f6f03",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss","Stage 2","Togekiss"],
    subtypes=["Stage 2"],
    collector_number=72,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    family_id=175,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    abilities=[
        Ability(
            title="Wonder Kiss",
            game_text="When your opponent's Active Pokémon is Knocked Out, flip a coin. If heads, take 1 more Prize card. The effect of Wonder Kiss doesn't stack.",
            passive=WonderKissPassive(),
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
