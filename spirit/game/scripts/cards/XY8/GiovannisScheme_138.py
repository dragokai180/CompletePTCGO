from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='df0f98f9-b058-544a-a2dd-c5f71f3f3f5f',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GiovannisScheme.Name',
    display_name="Giovanni's Scheme",
    searchable_by=["Giovanni's Scheme", 'Supporter', 'GiovannisScheme'],
    subtypes=['Supporter'],
    collector_number=138,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Choose 1:\n• Draw cards until you have 5 cards in your hand.\n• During this turn, your Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
    condition=standard_trainer_condition("Choose 1:\n• Draw cards until you have 5 cards in your hand.\n• During this turn, your Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
)
