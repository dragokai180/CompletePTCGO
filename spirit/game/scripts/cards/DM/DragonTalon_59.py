from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='992c7f18-3422-5fd5-9ae7-a6b78f90a5e2',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DragonTalon.Name',
    display_name='Dragon Talon',
    searchable_by=['Dragon Talon', 'Pokémon Tool', 'DragonTalon'],
    subtypes=['Pokémon Tool'],
    collector_number=59,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Dragon Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
