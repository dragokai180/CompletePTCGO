from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='b7ced02f-ca3b-5aaa-a021-a9a26ba63f12',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BuffPadding.Name',
    display_name='Buff Padding',
    searchable_by=['Buff Padding', 'Pokémon Tool', 'BuffPadding'],
    subtypes=['Pokémon Tool'],
    collector_number=136,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('If the Pokémon this card is attached to has a Retreat Cost of exactly 4, it gets +50 HP. You may play as many Item cards as you like during your turn (before your attack).'),
)
