from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f14bf81b-b33b-5bbe-a0a6-a04e8032438c',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GlalieSpiritLink.Name',
    display_name='Glalie Spirit Link',
    searchable_by=['Glalie Spirit Link', 'Pokémon Tool', 'GlalieSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=139,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Glalie-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
