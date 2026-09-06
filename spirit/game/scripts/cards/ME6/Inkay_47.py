from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand

async def knock_off(ctx):
    """10. Discard a random card from your opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)

card = PokemonCardDef(
    guid="9e6935ee-5087-5d6d-9e51-8b145f32d4bb",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay","Basic","Inkay"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=knock_off,
        ),
    ],
)
