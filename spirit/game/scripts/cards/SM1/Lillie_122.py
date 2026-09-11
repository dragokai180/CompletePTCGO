from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f3dd6105-4f4e-5cb9-bd8e-4b93ef6300b8',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name',
    display_name='Lillie',
    searchable_by=['Lillie', 'Supporter', 'Lillie'],
    subtypes=['Supporter'],
    collector_number=122,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw cards until you have 6 cards in your hand. If it's your first turn, draw cards until you have 8 cards in your hand."),
    condition=standard_trainer_condition("Draw cards until you have 6 cards in your hand. If it's your first turn, draw cards until you have 8 cards in your hand."),
)
