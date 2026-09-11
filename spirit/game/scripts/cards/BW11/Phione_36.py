from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def pull_out(ctx):
    """Put a card from your discard pile on top of your deck."""
    pile = ctx.discard_pile()
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, minimum=1,
        prompt="Choose a card to put on top of your deck",
    )
    if picks:
        await ctx.put_on_top_of_deck(picks[0])



card = PokemonCardDef(
    guid="765536ab-044a-5409-8f5f-6e560fba7841",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione","Basic","Phione"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Pull Out",
            game_text="Put a card from your discard pile on top of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pull_out,
        ),
        Attack(
            title="Aqua Boomerang",
            game_text="Return this Pokémon and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
    ],
)
