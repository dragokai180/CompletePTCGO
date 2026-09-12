from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='bea95630-268a-5101-bd9d-32d55a06f5ad',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name',
    display_name='Tropical Tidal Wave',
    searchable_by=['Tropical Tidal Wave', 'Item', 'TropicalTidalWave'],
    subtypes=['Item'],
    collector_number=18,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    attributes={200790: {'type': 'string', 'value': 'HGSS18'}},
    effect=standard_trainer_effect('Flip a coin. If heads, discard all Item and Stadium cards your opponent has in play. If tails, discard all Item and Stadium cards you have in play.'),
    condition=standard_trainer_condition('Flip a coin. If heads, discard all Item and Stadium cards your opponent has in play. If tails, discard all Item and Stadium cards you have in play.'),
)
