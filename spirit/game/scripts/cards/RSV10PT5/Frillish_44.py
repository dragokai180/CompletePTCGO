from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.session.effects import is_item_card

async def oceanic_gloom(ctx):
    """20 damage. During your opponent's next turn, they can't play any Item
    cards from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)

card = PokemonCardDef(
    guid="5f677644-bb14-5149-be28-23b82e3ba84d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    display_name="Frillish",
    searchable_by=["Frillish","Basic","Frillish"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=592,
    abilities=[
        Attack(
            title="Oceanic Gloom",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=oceanic_gloom,
        ),
    ],
)
