from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import boomerang_reattach

card = EnergyCardDef(
    guid="d199da70-33cd-540f-84b6-8ccb3d8bab54",
    key="SV06",
    name="Boomerang Energy",
    display_name="Boomerang Energy",
    searchable_by=["Boomerang Energy","Special","BoomerangEnergy"],
    subtypes=["Special"],
    collector_number=166,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_discarded_by_carrier_attack=boomerang_reattach,
)
