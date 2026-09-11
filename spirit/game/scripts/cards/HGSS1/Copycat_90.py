from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='2da4aa41-0645-5edf-8d35-91f7d41380c7',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name',
    display_name='Copycat',
    searchable_by=['Copycat', 'Supporter', 'Copycat'],
    subtypes=['Supporter'],
    collector_number=90,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand."),
    condition=standard_trainer_condition("You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand."),
)
