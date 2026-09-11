from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='31791748-c246-5d63-b8a0-595fde2b1f25',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.HoundoomSpiritLink.Name',
    display_name='Houndoom Spirit Link',
    searchable_by=['Houndoom Spirit Link', 'Pokémon Tool', 'HoundoomSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=142,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Houndoom-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
