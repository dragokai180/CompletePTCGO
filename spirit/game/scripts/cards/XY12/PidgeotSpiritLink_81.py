from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='7e0a1b1a-42f3-51d5-990b-ca969f82c375',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PidgeotSpiritLink.Name',
    display_name='Pidgeot Spirit Link',
    searchable_by=['Pidgeot Spirit Link', 'Pokémon Tool', 'PidgeotSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=81,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Pidgeot-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
