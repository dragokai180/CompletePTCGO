from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="c65bccdc-7c69-57a3-8d15-3faf6864b562",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCity.Name",
    display_name="Battle City",
    searchable_by=["Battle City","Stadium","BattleCity"],
    subtypes=["Stadium"],
    collector_number=39,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    passive=bw_trainer_passive('Battle City'),
    ability=bw_stadium_ability('Battle City'),
    abilities=bw_stadium_triggers('Battle City')
)
