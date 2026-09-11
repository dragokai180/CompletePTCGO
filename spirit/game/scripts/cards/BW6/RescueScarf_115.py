from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="194759b5-60eb-5d11-96f9-7554d94329a1",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueScarf.Name",
    display_name="Rescue Scarf",
    searchable_by=["Rescue Scarf","Pokémon Tool","Tool","RescueScarf"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=115,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Rescue Scarf'),
    granted_abilities=bw_tool_abilities('Rescue Scarf')
)
