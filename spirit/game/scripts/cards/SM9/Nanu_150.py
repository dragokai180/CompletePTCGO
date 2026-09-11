from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f91f713c-dd7e-59a5-9c62-6be92884231f',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Nanu.Name',
    display_name='Nanu',
    searchable_by=['Nanu', 'Supporter', 'Nanu'],
    subtypes=['Supporter'],
    collector_number=150,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose a Basic Darkness Pokémon in your discard pile. Switch it with 1 of your Pokémon in play. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.'),
    condition=standard_trainer_condition('Choose a Basic Darkness Pokémon in your discard pile. Switch it with 1 of your Pokémon in play. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.'),
)
