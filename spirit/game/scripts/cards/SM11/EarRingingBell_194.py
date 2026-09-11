from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='2d77f5bb-b373-5265-8b33-6902f10fffe8',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EarRingingBell.Name',
    display_name='Ear-Ringing Bell',
    searchable_by=['Ear-Ringing Bell', 'Pokémon Tool', 'EarRingingBell'],
    subtypes=['Pokémon Tool'],
    collector_number=194,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), the Attacking Pokémon is now Confused. You may play as many Item cards as you like during your turn (before your attack)."),
)
