from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='13c4fa65-fa0a-5248-b9f3-1ed5851b8e63',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SlowbroSpiritLink.Name',
    display_name='Slowbro Spirit Link',
    searchable_by=['Slowbro Spirit Link', 'Pokémon Tool', 'SlowbroSpiritLink'],
    subtypes=['Pokémon Tool'],
    collector_number=86,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('Your turn does not end if the Pokémon this card is attached to becomes M Slowbro-EX. You may play as many Item cards as you like during your turn (before your attack).'),
)
