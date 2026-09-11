from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='6f33598d-f004-59d4-b0e4-39ad40a09bea',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BigAirBalloon.Name',
    display_name='Big Air Balloon',
    searchable_by=['Big Air Balloon', 'Pokémon Tool', 'BigAirBalloon'],
    subtypes=['Pokémon Tool'],
    collector_number=155,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Stage 2 Pokémon this card is attached to has no Retreat Cost.'),
)
