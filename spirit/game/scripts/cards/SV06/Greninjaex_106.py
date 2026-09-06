from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.card_effects.attacks_common import snipe_attack


async def shinobi_blade(ctx):
    """170. Deal damage, then (optionally) search your deck."""
    await ctx.deal_damage()
    if not await ctx.ask_yes_no("Search your deck for a card and put it into your hand?"):
        return
    picks = await ctx.search_deck(
        count=1, minimum=0,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def mirage_barrage(ctx):
    """Discard 2 Energy, then 120 to 2 of your opponent's Pokémon.
    (No W/R for Benched Pokémon.)"""
    await ctx.discard_energy_from(
        ctx.attacker, 2,
        prompt="Choose 2 Energy to discard from this Pokémon",
    )
    await snipe_attack(
        120, pool="any", count=2,
        apply_modifiers=None,
    )(ctx)


card = PokemonCardDef(
    guid="f35bf2e6-bd20-4260-9423-a05a3acbbc08",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex", "Tera", "Greninjaex"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=106,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=656,
        evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Shinobi Blade",
            game_text="You may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=170,
            effect=shinobi_blade,
        ),
        Attack(
            title="Mirage Barrage",
            game_text=(
                "Discard 2 Energy from this Pokémon. "
                "This attack does 120 damage to 2 of your opponent's Pokémon. "
                "(Don't apply Weakness and Resistance for Benched Pokémon.)"
            ),
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=mirage_barrage,
        ),
    ],
)

