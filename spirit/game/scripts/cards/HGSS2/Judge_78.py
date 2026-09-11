from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='a9e7bc0c-c8dd-5c88-9c4e-d2e4fc0b03c9',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name',
    display_name='Judge',
    searchable_by=['Judge', 'Supporter', 'Judge'],
    subtypes=['Supporter'],
    collector_number=78,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Each player shuffles his or her hand into his or her deck and draws 4 cards.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Each player shuffles his or her hand into his or her deck and draws 4 cards.'),
)
