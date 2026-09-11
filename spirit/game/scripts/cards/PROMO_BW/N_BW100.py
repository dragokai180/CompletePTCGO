from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="4d483d2e-a05e-5b87-8990-c34c62119e1c",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N","Supporter","N"],
    subtypes=["Supporter"],
    collector_number=100,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    effect=bw_trainer_effect
)
