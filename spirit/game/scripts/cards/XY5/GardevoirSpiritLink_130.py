from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='85b0afde-b679-5336-a5a3-d02bc4e76729',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GardevoirSpiritLink.Name',
    display_name='Gardevoir Spirit Link',
    searchable_by=['Gardevoir Spirit Link', 'Pokémon Tool', 'GardevoirSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=130,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Gardevoir-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
