from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='6ae99315-490b-5117-9e06-db927d1bba0e',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GoodRod.Name',
    display_name='Good Rod',
    searchable_by=['Good Rod', 'Item', 'GoodRod'],
    subtypes=['Item'],
    collector_number=76,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, search your discard pile for a Pokémon, show it to your opponent, and put it on top of your deck. If tails, search your discard pile for an Item card, show it to your opponent, and put it on top of your deck.'),
    condition=standard_trainer_condition('Flip a coin. If heads, search your discard pile for a Pokémon, show it to your opponent, and put it on top of your deck. If tails, search your discard pile for an Item card, show it to your opponent, and put it on top of your deck.'),
)
