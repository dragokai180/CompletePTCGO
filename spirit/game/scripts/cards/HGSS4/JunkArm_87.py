from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='402bcc2a-5298-538d-8c97-7103eace63af',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.JunkArm.Name',
    display_name='Junk Arm',
    searchable_by=['Junk Arm', 'Item', 'JunkArm'],
    subtypes=['Item'],
    collector_number=87,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard 2 cards from your hand. Search your discard pile for an Item card, show it to your opponent, and put it into your hand. You can't choose Junk Arm with the effect of this card."),
    condition=standard_trainer_condition("Discard 2 cards from your hand. Search your discard pile for an Item card, show it to your opponent, and put it into your hand. You can't choose Junk Arm with the effect of this card."),
)
