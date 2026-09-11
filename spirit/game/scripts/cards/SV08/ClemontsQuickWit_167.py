from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="7fa050f1-4ae2-54a5-ba34-66989c387ef8",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClemontsQuickWit.Name",
    display_name="Clemont's Quick Wit",
    searchable_by=["Clemont's Quick Wit", "Supporter", "ClemontsQuickWit"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Heal 60 damage from each of your Lightning Pokémon."),
)
