from spirit.game.data_utils import PokemonCardDef, Attack, Ability, has_rule_box, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class _InitializationPassive(Passive):
    """Iron Thorns ex: while this Pokémon is Active, Rule Box Pokémon have
    no Abilities (except Future Pokémon)."""

    def blocks_abilities(self, pokemon, carrier):
        if not is_in_active_spot(carrier):
            return False
        if pokemon.entity_id == carrier.entity_id:
            return False
        if not has_rule_box(pokemon.archetype_id):
            return False
        return "Future" not in subtypes_for(pokemon.archetype_id)


async def volt_cyclone(ctx):
    """140. Move an Energy from this Pokémon to 1 of your Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1,
        prompt="Choose an Energy to move to 1 of your Benched Pokémon"
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="e737038e-ccba-4b8a-9901-e8bcc0fd933b",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronThornsex.Name",
    display_name="Iron Thorns ex",
    searchable_by=["Iron Thorns ex", "Basic", "ex", "IronThornsex"],
    subtypes=["Basic", "ex"],
    collector_number=77,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=995,
    abilities=[
        Ability(
            title="Initialization",
            game_text=(
                "As long as this Pokémon is in the Active Spot, Pokémon with a "
                "Rule Box in play (both yours and your opponent's) have no "
                "Abilities, except for Future Pokémon. "
                "(Pokémon ex, Pokémon V, etc. have Rule Boxes.)"
            ),
            passive=_InitializationPassive(),
        ),
        Attack(
            title="Volt Cyclone",
            game_text="Move an Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=volt_cyclone,
        ),
    ],
)

