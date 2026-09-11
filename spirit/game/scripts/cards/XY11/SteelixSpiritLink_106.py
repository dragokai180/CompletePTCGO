from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='41d2f013-7517-5d9d-919f-60b12a9c1f7b',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SteelixSpiritLink.Name',
    display_name='Steelix Spirit Link',
    searchable_by=['Steelix Spirit Link', 'Pokémon Tool', 'SteelixSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=106,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Steelix-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
