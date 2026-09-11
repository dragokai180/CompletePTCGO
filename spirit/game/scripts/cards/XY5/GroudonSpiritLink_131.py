from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='0184f277-0cee-5608-ac16-3e719b735552',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GroudonSpiritLink.Name',
    display_name='Groudon Spirit Link',
    searchable_by=['Groudon Spirit Link', 'Pokémon Tool', 'GroudonSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=131,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes Primal Groudon-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
