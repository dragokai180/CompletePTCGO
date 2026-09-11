from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='75dab4eb-d11f-50a6-b054-0086c77f4437',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LatiosSpiritLink.Name',
    display_name='Latios Spirit Link',
    searchable_by=['Latios Spirit Link', 'Pokémon Tool', 'LatiosSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=85,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Latios-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
