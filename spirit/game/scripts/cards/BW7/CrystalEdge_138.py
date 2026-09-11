from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="72d126ec-bc95-5c63-a4ee-2094d119d97a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalEdge.Name",
    display_name="Crystal Edge",
    searchable_by=["Crystal Edge","Pokémon Tool","Tool","ACE SPEC","CrystalEdge"],
    subtypes=["Pokémon Tool","Tool","ACE SPEC"],
    collector_number=138,
    set_code="BW7",
    rarity=Rarities.Ace,
    passive=bw_trainer_passive('Crystal Edge'),
    granted_abilities=bw_tool_abilities('Crystal Edge')
)
