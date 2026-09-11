from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='25628850-e253-5e25-a7d8-9282c01c76af',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Janine.Name',
    display_name='Janine',
    searchable_by=['Janine', 'Supporter', 'Janine'],
    subtypes=['Supporter'],
    collector_number=176,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 4 cards of your deck and put 2 of them into your hand. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('Look at the top 4 cards of your deck and put 2 of them into your hand. Shuffle the other cards back into your deck.'),
)
