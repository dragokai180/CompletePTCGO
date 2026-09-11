from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='28f11837-2e45-543d-8ec7-428ff0440a43',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WeaknessPolicy.Name',
    display_name='Weakness Policy',
    searchable_by=['Weakness Policy', 'Pokémon Tool', 'WeaknessPolicy'],
    subtypes=['Pokémon Tool'],
    collector_number=142,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Pokémon this card is attached to has no Weakness. You may play as many Item cards as you like during your turn (before your attack).'),
)
