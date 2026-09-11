from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='8abac291-21bd-5a5b-b36c-805cb16c68e6',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AerodactylSpiritLink.Name',
    display_name='Aerodactyl Spirit Link',
    searchable_by=['Aerodactyl Spirit Link', 'Pokémon Tool', 'AerodactylSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=99,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Aerodactyl-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
