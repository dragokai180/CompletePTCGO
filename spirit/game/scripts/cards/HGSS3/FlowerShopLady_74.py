from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ccfc1d5e-66ee-5ce6-a99f-cee383d90773',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FlowerShopLady.Name',
    display_name='Flower Shop Lady',
    searchable_by=['Flower Shop Lady', 'Supporter', 'FlowerShopLady'],
    subtypes=['Supporter'],
    collector_number=74,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Search your discard pile for 3 Pokémon and 3 basic Energy cards. Show them to your opponent and shuffle them into your deck.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Search your discard pile for 3 Pokémon and 3 basic Energy cards. Show them to your opponent and shuffle them into your deck.'),
)
