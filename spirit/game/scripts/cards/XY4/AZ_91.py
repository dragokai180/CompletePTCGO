from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='19230d7c-22ec-5261-baae-817ebad18999',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AZ.Name',
    display_name='AZ',
    searchable_by=['AZ', 'Supporter', 'AZ'],
    subtypes=['Supporter'],
    collector_number=91,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 1 Pokémon into your hand. (Discard all cards attached to that Pokémon.)'),
    condition=standard_trainer_condition('Put 1 Pokémon into your hand. (Discard all cards attached to that Pokémon.)'),
)
