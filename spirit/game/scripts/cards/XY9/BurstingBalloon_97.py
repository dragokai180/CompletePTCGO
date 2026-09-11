from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='65745751-0123-5aa3-aec1-f443028b5b9f',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BurstingBalloon.Name',
    display_name='Bursting Balloon',
    searchable_by=['Bursting Balloon', 'Pokémon Tool', 'BurstingBalloon'],
    subtypes=['Pokémon Tool'],
    collector_number=97,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn. If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), put 6 damage counters on the Attacking Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
