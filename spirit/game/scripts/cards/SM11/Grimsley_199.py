from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5d564d00-7915-550f-870e-394143551841',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Grimsley.Name',
    display_name='Grimsley',
    searchable_by=['Grimsley', 'Supporter', 'Grimsley'],
    subtypes=['Supporter'],
    collector_number=199,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Move up to 3 damage counters from 1 of your opponent's Pokémon to another of their Pokémon."),
    condition=standard_trainer_condition("Move up to 3 damage counters from 1 of your opponent's Pokémon to another of their Pokémon."),
)
