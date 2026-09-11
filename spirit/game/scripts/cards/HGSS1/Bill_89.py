from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='bf8550b2-7ea9-5195-aee6-b5d6773783a2',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name',
    display_name='Bill',
    searchable_by=['Bill', 'Supporter', 'Bill'],
    subtypes=['Supporter'],
    collector_number=89,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Draw 2 cards.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Draw 2 cards.'),
)
