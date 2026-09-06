from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import energy_recycler, has_basic_energy_in_discard


card = ItemCardDef(
    guid="7d8d48d4-2137-5701-8011-337d883a93a9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item", "EnergyRecycler"],
    subtypes=["Item"],
    collector_number=164,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=has_basic_energy_in_discard,
    effect=energy_recycler,
)
