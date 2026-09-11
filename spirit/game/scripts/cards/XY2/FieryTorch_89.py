from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='681e3241-8931-5029-ad89-4f87f4eac748',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FieryTorch.Name',
    display_name='Fiery Torch',
    searchable_by=['Fiery Torch', 'Item', 'FieryTorch'],
    subtypes=['Item'],
    collector_number=89,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard a Fire Energy card from your hand. (If you can't discard a Fire Energy card, you can't play this card.) Draw 2 cards. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Discard a Fire Energy card from your hand. (If you can't discard a Fire Energy card, you can't play this card.) Draw 2 cards. You may play as many Item cards as you like during your turn (before your attack)."),
)
