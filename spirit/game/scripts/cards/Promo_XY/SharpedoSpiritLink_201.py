from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='24a7f124-7f18-5fa3-ae7d-b9066c01728e',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SharpedoSpiritLink.Name',
    display_name='Sharpedo Spirit Link',
    searchable_by=['Sharpedo Spirit Link', 'Pokémon Tool', 'SharpedoSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=201,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Sharpedo-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
