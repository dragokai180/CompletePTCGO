from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='7b69fe43-db66-5d21-ac4c-038ba1cb2d18',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name',
    display_name='Lusamine ◇',
    searchable_by=['Lusamine ◇', 'Supporter', 'Prism Star', 'Lusamine'],
    subtypes=['Supporter', 'Prism Star'],
    collector_number=182,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Prism,
    effect=standard_trainer_effect("You can play this card only if your opponent has exactly 3 Prize cards remaining. Prevent all damage done to your Ultra Beasts by attacks during your opponent's next turn. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
    condition=standard_trainer_condition("You can play this card only if your opponent has exactly 3 Prize cards remaining. Prevent all damage done to your Ultra Beasts by attacks during your opponent's next turn. ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead."),
)
