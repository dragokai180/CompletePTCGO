from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.passives import carrier_pokemon


def _metal_holder(pokemon, carrier):
    holder = carrier_pokemon(carrier)
    if holder is not pokemon:
        return False
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.METAL.value in types


card = EnergyCardDef(
    guid="ee6accee-0629-5f76-8b93-66c6fc9b2e74",
    key="ME4",
    name="Magnetic Metal Energy",
    display_name="Magnetic Metal Energy",
    searchable_by=["Magnetic Metal Energy","Special","MagneticMetalEnergy"],
    subtypes=["Special"],
    collector_number=85,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    passive=retreat_free_when(_metal_holder),
)
