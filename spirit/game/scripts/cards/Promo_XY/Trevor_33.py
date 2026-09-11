from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='215733d5-9be6-58bd-a058-252d1a91c14f',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Trevor.Name',
    display_name='Trevor',
    searchable_by=['Trevor', 'Supporter', 'Trevor'],
    subtypes=['Supporter'],
    collector_number=33,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    effect=standard_trainer_effect('Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.'),
)
