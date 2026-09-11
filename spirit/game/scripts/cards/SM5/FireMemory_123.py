from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='8afdad31-00e1-5bda-8783-d78c6d984f70',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FireMemory.Name',
    display_name='Fire Memory',
    searchable_by=['Fire Memory', 'Pokémon Tool', 'FireMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=123,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Silvally-GX this card is attached to is a Fire Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
