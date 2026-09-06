from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.session.passives import carrier_pokemon


def _water_holder(target, carrier):
    holder = carrier_pokemon(carrier)
    if holder is not target:
        return False
    types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.WATER.value in types


async def bubbly_water_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is None:
        return
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.WATER.value in types:
        await ctx.cure_all_conditions(pokemon)


card = EnergyCardDef(
    guid="d5d4bb36-5bcd-50cd-be33-68d42d985b2f",
    key="ME4",
    name="Bubbly Water Energy",
    display_name="Bubbly Water Energy",
    searchable_by=["Bubbly Water Energy","Special","BubblyWaterEnergy"],
    subtypes=["Special"],
    collector_number=84,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.WATER,
    is_special=True,
    on_attach=bubbly_water_on_attach,
    passive=condition_immunity_passive(protects=_water_holder),
)
