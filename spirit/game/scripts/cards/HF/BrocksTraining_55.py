from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c9f5e4ac-36a4-5da9-acf1-d84198fbd72e',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BrocksTraining.Name',
    display_name="Brock's Training",
    searchable_by=["Brock's Training", 'Supporter', 'BrocksTraining'],
    subtypes=['Supporter'],
    collector_number=55,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('Attach an Energy card from your hand to 1 of your Geodude, Graveler, Golem, Onix-GX, Cubone, Rhyhorn, Rhydon, or Sudowoodo.'),
    condition=standard_trainer_condition('Attach an Energy card from your hand to 1 of your Geodude, Graveler, Golem, Onix-GX, Cubone, Rhyhorn, Rhydon, or Sudowoodo.'),
)
