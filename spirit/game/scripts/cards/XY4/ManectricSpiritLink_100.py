from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='fa812de4-0871-5201-9b8e-53ea9e91f32a',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ManectricSpiritLink.Name',
    display_name='Manectric Spirit Link',
    searchable_by=['Manectric Spirit Link', 'Pokémon Tool', 'ManectricSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=100,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Manectric-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
