from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="de2772ee-ed13-56d2-a2b3-b8dc1e726c47",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantCape.Name",
    display_name="Giant Cape",
    searchable_by=["Giant Cape","Pokémon Tool","Tool","GiantCape"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=114,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Giant Cape'),
    granted_abilities=bw_tool_abilities('Giant Cape')
)
