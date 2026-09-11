from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='b147176c-6cc4-5ca0-83ec-2758185bf986',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.UTurnBoard.Name',
    display_name='U-Turn Board',
    searchable_by=['U-Turn Board', 'Pokémon Tool', 'UTurnBoard'],
    subtypes=['Pokémon Tool'],
    collector_number=211,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Retreat Cost of the Pokémon this card is attached to is Colorless less. If this card is discarded from play, put it into your hand instead of the discard pile. You may play as many Item cards as you like during your turn (before your attack).'),
)
