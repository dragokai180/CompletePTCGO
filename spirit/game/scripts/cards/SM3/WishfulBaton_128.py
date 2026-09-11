from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='8b7be871-bcc3-52e3-980b-f90ef44e0922',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WishfulBaton.Name',
    display_name='Wishful Baton',
    searchable_by=['Wishful Baton', 'Pokémon Tool', 'WishfulBaton'],
    subtypes=['Pokémon Tool'],
    collector_number=128,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is your Active Pokémon and is Knocked Out by damage from an opponent's attack, move up to 3 basic Energy cards from that Pokémon to 1 of your Benched Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
