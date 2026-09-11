from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='fd0a2e78-87ee-5940-a26b-e206cbe90d30',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BillsTransfer.Name',
    display_name="Bill's Transfer",
    searchable_by=["Bill's Transfer", 'Supporter', 'BillsTransfer'],
    subtypes=['Supporter'],
    collector_number=156,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 8 cards of your deck. You may reveal any number of Pokémon you find there and put them into your hand. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('Look at the top 8 cards of your deck. You may reveal any number of Pokémon you find there and put them into your hand. Shuffle the other cards back into your deck.'),
)
