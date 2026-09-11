from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='089f8d41-b5de-55f7-a75a-4d72775738be',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Dendra.Name',
    display_name='Dendra',
    searchable_by=['Dendra', 'Supporter', 'Dendra'],
    subtypes=['Supporter'],
    collector_number=179,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put a card from your hand on the bottom of your deck. If you do, draw cards until you have 5 cards in your hand.\xa0(If you have no other cards in your hand, you can't use this card.)"),
    condition=standard_trainer_condition("Put a card from your hand on the bottom of your deck. If you do, draw cards until you have 5 cards in your hand.\xa0(If you have no other cards in your hand, you can't use this card.)"),
)
