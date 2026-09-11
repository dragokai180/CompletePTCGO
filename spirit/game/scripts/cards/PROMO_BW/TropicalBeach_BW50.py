from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="96cb9e70-2675-5489-b133-2f3f1d795aa9",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalBeach.Name",
    display_name="Tropical Beach",
    searchable_by=["Tropical Beach","Stadium","TropicalBeach"],
    subtypes=["Stadium"],
    collector_number=50,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    passive=bw_trainer_passive('Tropical Beach'),
    ability=bw_stadium_ability('Tropical Beach'),
    abilities=bw_stadium_triggers('Tropical Beach')
)
