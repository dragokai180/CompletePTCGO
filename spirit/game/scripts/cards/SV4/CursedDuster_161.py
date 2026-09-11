from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='84ae80d7-8887-52ac-8a99-671671cfc0fd',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CursedDuster.Name',
    display_name='Cursed Duster',
    searchable_by=['Cursed Duster', 'Pokémon Tool', 'CursedDuster'],
    subtypes=['Pokémon Tool'],
    collector_number=161,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("If the Pokémon this card is attached to is Knocked Out by damage from an attack from your opponent's Pokémon, discard a random card from your opponent's hand."),
)
