from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='3e6a37da-7286-5304-b7d5-41a369fa2e9a',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name',
    display_name='Fisherman',
    searchable_by=['Fisherman', 'Supporter', 'Fisherman'],
    subtypes=['Supporter'],
    collector_number=136,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 4 basic Energy cards from your discard pile into your hand.'),
    condition=standard_trainer_condition('Put 4 basic Energy cards from your discard pile into your hand.'),
)
