from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='2a8eddad-33cc-53b3-adbc-b1517bece3c3',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GalladeSpiritLink.Name',
    display_name='Gallade Spirit Link',
    searchable_by=['Gallade Spirit Link', 'Pokémon Tool', 'GalladeSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=83,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Gallade-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
