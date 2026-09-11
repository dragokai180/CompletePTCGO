from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='8bbdf369-8699-5d83-8207-40cda6b434b6',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Ilima.Name',
    display_name='Ilima',
    searchable_by=['Ilima', 'Supporter', 'Ilima'],
    subtypes=['Supporter'],
    collector_number=121,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Each player shuffles their hand into their deck and flips a coin. If heads, that player draws 6 cards. If tails, they draw 3 cards.'),
    condition=standard_trainer_condition('Each player shuffles their hand into their deck and flips a coin. If heads, that player draws 6 cards. If tails, they draw 3 cards.'),
)
