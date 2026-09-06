from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities


async def terminal_period(ctx):
    """If your opponent's Active Pokémon has exactly 6 damage counters on
    it, that Pokémon is Knocked Out."""
    defender = ctx.defender
    if defender is None:
        return
    counters = max(0, (ctx.max_hp(defender) - defender.get_attribute(AttrID.HP, 0)) // 10)
    if counters == 6:
        await ctx.knock_out(defender)


async def claw_of_darkness(ctx):
    """200. Your opponent reveals their hand, and you discard a card you
    find there."""
    await ctx.deal_damage()
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card to discard from your opponent's hand.",
        display_cards=hand,
    )
    await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="7cf0bdd0-6b3b-5ff6-b0ce-3e8774add352",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAbsolex.Name",
    display_name="Mega Absol ex",
    searchable_by=["Mega Absol ex","Basic","ex","SV_Mega","MegaAbsolex"],
    subtypes=["Basic","ex","SV_Mega"],
    collector_number=86,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    family_id=359,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Attack(
            title="Terminal Period",
            game_text="If your opponent's Active Pokémon has exactly 6 damage counters on it, that Pokémon is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=terminal_period,
        ),
        Attack(
            title="Claw of Darkness",
            game_text="Your opponent reveals their hand, and you discard a card you find there.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=claw_of_darkness,
        ),
    ],
)
