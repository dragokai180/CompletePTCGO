from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='999af1e2-d460-56b7-b812-18dcfed40236',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Mallow.Name',
    display_name='Mallow',
    searchable_by=['Mallow', 'Supporter', 'Mallow'],
    subtypes=['Supporter'],
    collector_number=127,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for 2 cards, shuffle your deck, and put those cards on top of your deck in any order.'),
    condition=standard_trainer_condition('Search your deck for 2 cards, shuffle your deck, and put those cards on top of your deck in any order.'),
)
