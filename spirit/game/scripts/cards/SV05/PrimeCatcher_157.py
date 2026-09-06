from spirit.game.card_effects.trainers import catcher_switch_both, opponent_has_bench
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


card = ItemCardDef(
    guid="b6707998-5001-51da-8fc1-0eccbbe1fde8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrimeCatcher.Name",
    display_name="Prime Catcher",
    searchable_by=["Prime Catcher", "Item", "ACE SPEC", "PrimeCatcher"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=157,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    effect=catcher_switch_both,
    condition=opponent_has_bench,
)
