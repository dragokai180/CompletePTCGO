from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='0f5a1f20-cd44-578b-9b9d-a1c8481903b5',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.IngoEmmet.Name',
    display_name='Ingo & Emmet',
    searchable_by=['Ingo & Emmet', 'Supporter', 'IngoEmmet'],
    subtypes=['Supporter'],
    collector_number=144,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top card of your deck, and then choose 1:\n• Discard your hand and draw 5 cards.\n• Discard your hand and draw 5 cards from the bottom of your deck.'),
    condition=standard_trainer_condition('Look at the top card of your deck, and then choose 1:\n• Discard your hand and draw 5 cards.\n• Discard your hand and draw 5 cards from the bottom of your deck.'),
)
