from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='5d2a67b8-622d-59ef-96e3-98568fd23577',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.AmpharosSpiritLink.Name',
    display_name='Ampharos Spirit Link',
    searchable_by=['Ampharos Spirit Link', 'Pokémon Tool', 'AmpharosSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=70,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Ampharos-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
