from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


async def ground_melter(ctx):
    """60, +60 more if a Stadium is in play; then discard that Stadium."""
    stadium = ctx.stadium_in_play()
    amount = 60 + (60 if stadium is not None else 0)
    await ctx.deal_damage(amount)
    if stadium is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="9a274e93-c320-5f62-a343-658f7a769926",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic", "ChiYu"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Allure",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Ground Melter",
            game_text="If a Stadium is in play, this attack does 60 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ground_melter,
        ),
    ],
)
