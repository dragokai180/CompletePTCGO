from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="f975ed78-41cc-5739-9a23-c063368516d7",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eviolite.Name",
    display_name="Eviolite",
    searchable_by=["Eviolite","Pokémon Tool","Tool","Eviolite"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=91,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Eviolite'),
    granted_abilities=bw_tool_abilities('Eviolite')
)
