from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="b0c9b3c9-9d9d-55ef-9c08-630e46ecdb3f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkClaw.Name",
    display_name="Dark Claw",
    searchable_by=["Dark Claw","Pokémon Tool","Tool","DarkClaw"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=92,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Dark Claw'),
    granted_abilities=bw_tool_abilities('Dark Claw')
)
