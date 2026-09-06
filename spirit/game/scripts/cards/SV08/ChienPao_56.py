from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import pumpkin_pit

async def icicle_loop(ctx):
    """120. Put an Energy attached to this Pokémon into your hand."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.source)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)

card = PokemonCardDef(
    guid="f273d667-2d49-5488-805d-ffdf75fb75b9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name",
    display_name="Chien-Pao",
    searchable_by=["Chien-Pao","Basic","ChienPao"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    family_id=1002,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Ability(
            title="Snow Sink",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Stadium in play.",
            trigger=Triggers.ON_PLAY,
            effect=pumpkin_pit,
        ),
        Attack(
            title="Icicle Loop",
            game_text="Put an Energy attached to this Pokémon into your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=icicle_loop,
        ),
    ],
)
