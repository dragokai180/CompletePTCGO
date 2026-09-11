from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='10fcc41f-db20-5a45-8a20-c144cb23836a',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SceptileSpiritLink.Name',
    display_name='Sceptile Spirit Link',
    searchable_by=['Sceptile Spirit Link', 'Pokémon Tool', 'SceptileSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=80,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Sceptile-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
