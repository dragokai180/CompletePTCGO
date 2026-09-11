from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="2e6782c8-309d-59f9-b567-fae0359eac7a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pokémon Center","Stadium","PokmonCenter"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Pokémon Center'),
    ability=bw_stadium_ability('Pokémon Center'),
    abilities=bw_stadium_triggers('Pokémon Center')
)
