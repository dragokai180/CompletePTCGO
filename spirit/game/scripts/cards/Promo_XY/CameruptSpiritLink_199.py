from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='cadfe4a4-853d-56c7-904c-2dd342b39545',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CameruptSpiritLink.Name',
    display_name='Camerupt Spirit Link',
    searchable_by=['Camerupt Spirit Link', 'Pokémon Tool', 'CameruptSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=199,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Camerupt-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
