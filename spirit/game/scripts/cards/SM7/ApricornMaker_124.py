from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='84ac64f4-d478-5575-8ab3-7137074956dc',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name',
    display_name='Apricorn Maker',
    searchable_by=['Apricorn Maker', 'Supporter', 'ApricornMaker'],
    subtypes=['Supporter'],
    collector_number=124,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 Item cards that have the word "Ball" in their name, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 2 Item cards that have the word "Ball" in their name, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
