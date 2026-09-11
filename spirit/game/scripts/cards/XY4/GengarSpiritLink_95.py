from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='d58378e9-5177-5aa3-8e33-3e99bb9a29ae',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GengarSpiritLink.Name',
    display_name='Gengar Spirit Link',
    searchable_by=['Gengar Spirit Link', 'Pokémon Tool', 'GengarSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=95,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Gengar-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
