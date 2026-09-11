from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='df46868a-bfab-5571-afec-ddea0d59691e',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.VenusaurSpiritLink.Name',
    display_name='Venusaur Spirit Link',
    searchable_by=['Venusaur Spirit Link', 'Pokémon Tool', 'VenusaurSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=89,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Venusaur-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
