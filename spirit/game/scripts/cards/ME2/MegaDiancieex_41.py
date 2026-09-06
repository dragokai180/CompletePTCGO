from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive


async def garland_ray(ctx):
    """Discard up to 2 Energy cards from this Pokémon, and this attack does
    120 damage for each card you discarded in this way."""
    discarded = []
    if ctx.attached_energies(ctx.attacker) and await ctx.ask_yes_no(
            "Discard up to 2 Energy from this Pokémon?"):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 2, minimum=0,
            prompt="Choose up to 2 Energy to discard")
    amount = 120 * len(discarded)
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="e48063b5-0eeb-57cb-8597-69f210345b7b",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDiancieex.Name",
    display_name="Mega Diancie ex",
    searchable_by=["Mega Diancie ex","Basic","ex","SV_Mega","MegaDiancieex"],
    subtypes=["Basic","ex","SV_Mega"],
    collector_number=41,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=719,
    abilities=[
        Ability(
            title="Diamond Coat",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Garland Ray",
            game_text="Discard up to 2 Energy cards from this Pokémon, and this attack does 120 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            damage_operator="x",
            effect=garland_ray,
        ),
    ],
)
