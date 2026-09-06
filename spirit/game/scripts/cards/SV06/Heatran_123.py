from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.pokemon import energy_provides_type, in_active_spot


async def incandescent_body(ctx):
    """If this Pokémon is in the Active Spot and is damaged by an attack from
    your opponent's Pokémon (even if this Pokémon is Knocked Out), the
    Attacking Pokémon is now Burned."""
    pokemon = ctx.source
    if not in_active_spot(ctx.board, ctx.player_id, pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.BURNED)


async def steel_burst(ctx):
    """Discard all Metal Energy from this Pokémon. 50 damage per card
    discarded."""
    metal = [
        energy for energy in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(energy, PokemonTypes.METAL.value)
    ]
    if metal:
        await ctx.discard_cards(metal)
    amount = 50 * len(metal)
    if amount:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="ac2dbd77-bcf4-5e37-aa4a-4f1c5f8b26b1",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran","Basic","Heatran"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    family_id=485,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    abilities=[
        Ability(
            title="Incandescent Body",
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=incandescent_body,
        ),
        Attack(
            title="Steel Burst",
            game_text="Discard all Metal Energy from this Pokémon. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=steel_burst,
        ),
    ],
)
