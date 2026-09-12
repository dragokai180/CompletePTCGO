from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="2bd08d2b-fa60-5277-8f58-7cb39aa5cc08",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaBadge.Name",
    display_name="Team Plasma Badge",
    searchable_by=["Team Plasma Badge","Pokémon Tool","Tool","TeamPlasmaBadge"],
    subtypes=["Pokémon Tool","Tool","Team Plasma"],
    collector_number=104,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Team Plasma Badge'),
    granted_abilities=bw_tool_abilities('Team Plasma Badge')
)
