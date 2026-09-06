from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card


async def itchy_pollen(ctx):
    """10 damage. During your opponent's next turn, they can't play any Item
    cards from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="bdef4ae9-501d-5c42-8c31-0f68b18233fc",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name",
    display_name="Budew",
    searchable_by=["Budew", "Basic", "Budew"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=406,
    abilities=[
        Attack(
            title="Itchy Pollen",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={},
            damage=10,
            effect=itchy_pollen,
        ),
    ],
)
