from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="7c2465fb-3fe7-5bb8-9f47-13dac29ad29b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockGuard.Name",
    display_name="Rock Guard",
    searchable_by=["Rock Guard","Pokémon Tool","Tool","ACE SPEC","RockGuard"],
    subtypes=["Pokémon Tool","Tool","ACE SPEC"],
    collector_number=108,
    set_code="BW9",
    rarity=Rarities.Ace,
    passive=bw_trainer_passive('Rock Guard'),
    granted_abilities=bw_tool_abilities('Rock Guard')
)
