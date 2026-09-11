from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='04c7d732-8c5b-524e-a91b-7ac646cc7f9e',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EmceesChatter.Name',
    display_name="Emcee's Chatter",
    searchable_by=["Emcee's Chatter", 'Supporter', 'EmceesChatter'],
    subtypes=['Supporter'],
    collector_number=73,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Flip a coin. If heads, draw 3 cards. If tails, draw 2 cards.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Flip a coin. If heads, draw 3 cards. If tails, draw 2 cards.'),
)
