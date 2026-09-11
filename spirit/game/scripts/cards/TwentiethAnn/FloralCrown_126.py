from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='9ab49a52-5b8a-5019-9d63-c5e6a7855dd3',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FloralCrown.Name',
    display_name='Floral Crown',
    searchable_by=['Floral Crown', 'Pokémon Tool', 'FloralCrown'],
    subtypes=['Pokémon Tool'],
    collector_number=126,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    passive=standard_passive("At the end of your opponent's turn, heal 20 damage from the Basic Pokémon this card is attached to. You may play as many Item cards as you like during your turn (before your attack)."),
)
