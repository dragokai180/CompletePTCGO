from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='06ef6071-19b1-5271-bd2f-75c68a9a5529',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name',
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", 'Supporter', 'MistysDetermination'],
    subtypes=['Supporter'],
    collector_number=104,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard a card from your hand. If you do, look at the top 8 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('Discard a card from your hand. If you do, look at the top 8 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.'),
)
