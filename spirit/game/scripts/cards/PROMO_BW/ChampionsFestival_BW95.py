from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="2bf36470-e0ed-5ace-8902-e76fba2b0ec0",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival","Stadium","ChampionsFestival"],
    subtypes=["Stadium"],
    collector_number=95,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    passive=bw_trainer_passive('Champions Festival'),
    ability=bw_stadium_ability('Champions Festival'),
    abilities=bw_stadium_triggers('Champions Festival')
)
