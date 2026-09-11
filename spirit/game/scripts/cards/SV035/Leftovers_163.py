from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='2e4c254c-2ba6-5da3-b384-20f321a87b9a',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Leftovers.Name',
    display_name='Leftovers',
    searchable_by=['Leftovers', 'Pokémon Tool', 'Leftovers'],
    subtypes=['Pokémon Tool'],
    collector_number=163,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('At the end of your turn, if the Pokémon this card is attached to is in the Active Spot, heal 20 damage from it.'),
)
