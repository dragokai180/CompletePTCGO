from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='965ced53-6273-5689-96a0-b65727349df4',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GarchompSpiritLink.Name',
    display_name='Garchomp Spirit Link',
    searchable_by=['Garchomp Spirit Link', 'Pokémon Tool', 'GarchompSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=169,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Garchomp-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
