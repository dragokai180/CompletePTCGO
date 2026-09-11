from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e1d35f01-14f2-5c86-9c1b-5e95f19ac948',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergyExchanger.Name',
    display_name='Energy Exchanger',
    searchable_by=['Energy Exchanger', 'Item', 'EnergyExchanger'],
    subtypes=['Item'],
    collector_number=73,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose an Energy card from your hand, show it to your opponent, and put it on top of your deck. Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Choose an Energy card from your hand, show it to your opponent, and put it on top of your deck. Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
)
