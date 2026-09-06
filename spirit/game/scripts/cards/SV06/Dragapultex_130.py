from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive


async def phantom_dive(ctx):
    """200. Put 6 damage counters on the opponent's Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    await ctx.place_damage_counters(6, candidates=bench)


card = PokemonCardDef(
    guid="ebb535cb-faab-4642-aa4e-4077c6a879a0",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapultex.Name",
    display_name="Dragapult ex",
    searchable_by=["Dragapult ex", "Stage 2", "ex", "Tera", "Dragapultex"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=130,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
        Attack(
            title="Phantom Dive",
            game_text="Put 6 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=200,
            effect=phantom_dive,
        ),
    ],
)

