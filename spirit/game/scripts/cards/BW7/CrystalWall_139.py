from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="a0d9688a-ccfc-5803-ac3c-59fb5d05933f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalWall.Name",
    display_name="Crystal Wall",
    searchable_by=["Crystal Wall","Pokémon Tool","Tool","ACE SPEC","CrystalWall"],
    subtypes=["Pokémon Tool","Tool","ACE SPEC"],
    collector_number=139,
    set_code="BW7",
    rarity=Rarities.Ace,
    passive=bw_trainer_passive('Crystal Wall'),
    granted_abilities=bw_tool_abilities('Crystal Wall')
)
