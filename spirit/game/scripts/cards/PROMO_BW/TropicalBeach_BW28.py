from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="00e32750-f213-5b23-b831-32571ec1aaa1",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalBeach.Name",
    display_name="Tropical Beach",
    searchable_by=["Tropical Beach","Stadium","TropicalBeach"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    passive=bw_trainer_passive('Tropical Beach'),
    ability=bw_stadium_ability('Tropical Beach'),
    abilities=bw_stadium_triggers('Tropical Beach')
)
