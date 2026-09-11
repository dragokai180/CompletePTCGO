from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='60363378-785f-56fb-9abe-55a1e4219a06',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BillsAnalysis.Name',
    display_name="Bill's Analysis",
    searchable_by=["Bill's Analysis", 'Supporter', 'BillsAnalysis'],
    subtypes=['Supporter'],
    collector_number=133,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('Look at the top 7 cards of your deck. You may reveal up to 2 Trainer cards you find there and put them into your hand. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('Look at the top 7 cards of your deck. You may reveal up to 2 Trainer cards you find there and put them into your hand. Shuffle the other cards back into your deck.'),
)
