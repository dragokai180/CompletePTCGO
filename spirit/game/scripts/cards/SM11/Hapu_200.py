from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='b4863af3-49c5-51d7-af22-66305e1bba37',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Hapu.Name',
    display_name='Hapu',
    searchable_by=['Hapu', 'Supporter', 'Hapu'],
    subtypes=['Supporter'],
    collector_number=200,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 6 cards of your deck and put 2 of them into your hand. Discard the other cards.'),
    condition=standard_trainer_condition('Look at the top 6 cards of your deck and put 2 of them into your hand. Discard the other cards.'),
)
