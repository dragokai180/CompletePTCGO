from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='af452ef5-816d-5fb1-b824-375a7e1ddbd1',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SagesTraining.Name',
    display_name="Sage's Training",
    searchable_by=["Sage's Training", 'Supporter', 'SagesTraining'],
    subtypes=['Supporter'],
    collector_number=77,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Look at the top 5 cards of your deck. Choose any 2 cards you find there and put them into your hand. Discard the other cards.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Look at the top 5 cards of your deck. Choose any 2 cards you find there and put them into your hand. Discard the other cards.'),
)
