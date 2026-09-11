from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ea70ea85-89a6-5b5b-87c8-55c229b32ed7',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name',
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", 'Supporter', 'SabrinasSuggestion'],
    subtypes=['Supporter'],
    collector_number=154,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals their hand. You may choose a Supporter card you find there and use the effect of that card as the effect of this card.'),
    condition=standard_trainer_condition('Your opponent reveals their hand. You may choose a Supporter card you find there and use the effect of that card as the effect of this card.'),
)
