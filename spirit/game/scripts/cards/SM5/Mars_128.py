from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='995329f5-c227-5f4b-b551-b7e25bef0985',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name',
    display_name='Mars',
    searchable_by=['Mars', 'Supporter', 'Mars'],
    subtypes=['Supporter'],
    collector_number=128,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 2 cards. If you do, discard a random card from your opponent's hand."),
    condition=standard_trainer_condition("Draw 2 cards. If you do, discard a random card from your opponent's hand."),
)
