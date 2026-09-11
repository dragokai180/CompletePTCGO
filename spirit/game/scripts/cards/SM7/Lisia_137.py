from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='170666de-07f5-5edf-9be1-f084cf6c13d1',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name',
    display_name='Lisia',
    searchable_by=['Lisia', 'Supporter', 'Lisia'],
    subtypes=['Supporter'],
    collector_number=137,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 ◇ (Prism Star) cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 2 ◇ (Prism Star) cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
