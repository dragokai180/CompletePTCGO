from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="a56be50f-cbcd-52d4-bf26-809a91cafd03",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pokémon Communication","Item","PokmonCommunication"],
    subtypes=["Item"],
    collector_number=99,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
