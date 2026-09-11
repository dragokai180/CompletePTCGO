from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='2c1ddbf0-e0e9-5a3c-a071-52f5553dea7b',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BeedrillSpiritLink.Name',
    display_name='Beedrill Spirit Link',
    searchable_by=['Beedrill Spirit Link', 'Pokémon Tool', 'BeedrillSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=159,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Beedrill-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
