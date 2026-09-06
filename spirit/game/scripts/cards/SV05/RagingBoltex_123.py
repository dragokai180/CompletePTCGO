from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import discard_then_draw


async def bellowing_thunder(ctx):
    """You may discard any amount of Basic Energy from your Pokémon; 70
    damage for each card discarded this way."""
    candidates = [
        e for p in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(p)
        if is_basic_energy_card(e)
    ]
    picks = []
    if candidates:
        picks = await ctx.choose_cards(
            candidates, len(candidates), minimum=0,
            prompt="Discard any amount of Basic Energy from your Pokémon.",
        )
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(70 * len(picks))


card = PokemonCardDef(
    guid="2b2def13-588d-536a-9c24-d0617a41af2f",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RagingBoltex.Name",
    display_name="Raging Bolt ex",
    searchable_by=["Raging Bolt ex", "Basic", "ex", "Ancient", "RagingBoltex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=123,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=1021,
    abilities=[
        Attack(
            title="Burst Roar",
            game_text="Discard your hand and draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_then_draw(None, 6, whole_hand=True),
        ),
        Attack(
            title="Bellowing Thunder",
            game_text="You may discard any amount of Basic Energy from your Pokémon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="x",
            effect=bellowing_thunder,
        ),
    ],
)
