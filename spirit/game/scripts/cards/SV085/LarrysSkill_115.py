from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="5ba70314-81c7-5dfb-a864-e054e92c2a07",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LarrysSkill.Name",
    display_name="Larry's Skill",
    searchable_by=["Larry's Skill", "Supporter", "LarrysSkill"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Discard your hand and search your deck for a Pokémon, a Supporter card, and a Basic Energy card, reveal them, and put them into your hand. Then, shuffle your deck."),
)
