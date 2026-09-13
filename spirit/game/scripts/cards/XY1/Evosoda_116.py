from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.trainer_followup import evosoda, evosoda_condition
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='180b57c2-e73c-5589-86fb-7242717055e6',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Evosoda.Name',
    display_name='Evosoda',
    searchable_by=['Evosoda', 'Item', 'Evosoda'],
    subtypes=['Item'],
    collector_number=116,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=evosoda,
    condition=evosoda_condition,
)
