from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='f2ed3342-ea03-5e98-954b-538ad8f79f09',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BlastoiseSpiritLink.Name',
    display_name='Blastoise Spirit Link',
    searchable_by=['Blastoise Spirit Link', 'Pokémon Tool', 'BlastoiseSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=73,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Blastoise-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
