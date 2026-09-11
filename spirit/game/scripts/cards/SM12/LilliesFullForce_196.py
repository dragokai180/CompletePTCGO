from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c34a3e29-428e-5f49-a6de-279f4999c6e3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LilliesFullForce.Name',
    display_name="Lillie's Full Force",
    searchable_by=["Lillie's Full Force", 'Supporter', 'LilliesFullForce'],
    subtypes=['Supporter'],
    collector_number=196,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 4 cards. At the end of this turn, if you have 3 or more cards in your hand, shuffle cards from your hand into your deck until you have 2 cards in your hand.'),
    condition=standard_trainer_condition('Draw 4 cards. At the end of this turn, if you have 3 or more cards in your hand, shuffle cards from your hand into your deck until you have 2 cards in your hand.'),
)
