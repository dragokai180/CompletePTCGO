from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f05087b3-ca20-5ec4-b850-b5db64d3d28b',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SparklingRobe.Name',
    display_name='Sparkling Robe',
    searchable_by=['Sparkling Robe', 'Pokémon Tool', 'SparklingRobe'],
    subtypes=['Pokémon Tool'],
    collector_number=99,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Pokémon this card is attached to can't be affected by any Special Conditions. (Remove any Special Conditions affecting that Pokémon.) You may play as many Item cards as you like during your turn (before your attack)."),
)
