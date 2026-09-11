from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='dfdaaf6f-f76d-50d3-9cb5-f96775892a35',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AltariaSpiritLink.Name',
    display_name='Altaria Spirit Link',
    searchable_by=['Altaria Spirit Link', 'Pokémon Tool', 'AltariaSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=91,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Altaria-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
