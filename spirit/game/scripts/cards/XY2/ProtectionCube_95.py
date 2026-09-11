from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='460abd81-5454-5c75-9c5b-c6e4abc88cf3',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProtectionCube.Name',
    display_name='Protection Cube',
    searchable_by=['Protection Cube', 'Pokémon Tool', 'ProtectionCube'],
    subtypes=['Pokémon Tool'],
    collector_number=95,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Prevent all damage done to the Pokémon this card is attached to by attacks it uses. You may play as many Item cards as you like during your turn (before your attack).'),
)
