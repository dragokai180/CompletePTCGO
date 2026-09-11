from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='97afc8bc-4058-5226-a109-58e7ee8cfa6a',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BeastBall.Name',
    display_name='Beast Ball',
    searchable_by=['Beast Ball', 'Item', 'BeastBall'],
    subtypes=['Item'],
    collector_number=125,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at your face-down Prize cards. You may reveal an Ultra Beast card you find there, put it into your hand, and put this Beast Ball in its place. (If you don't reveal an Ultra Beast card, put this card in the discard pile.) Then, shuffle your face-down Prize cards. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Look at your face-down Prize cards. You may reveal an Ultra Beast card you find there, put it into your hand, and put this Beast Ball in its place. (If you don't reveal an Ultra Beast card, put this card in the discard pile.) Then, shuffle your face-down Prize cards. You may play as many Item cards as you like during your turn (before your attack)."),
)
