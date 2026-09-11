from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="2806afe9-470b-5e2a-97fc-70e5f49720a3",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TwistMountain.Name",
    display_name="Twist Mountain",
    searchable_by=["Twist Mountain","Stadium","TwistMountain"],
    subtypes=["Stadium"],
    collector_number=101,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Twist Mountain'),
    ability=bw_stadium_ability('Twist Mountain'),
    abilities=bw_stadium_triggers('Twist Mountain')
)
