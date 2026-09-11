from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='759189e4-6984-573c-89a8-e8c0075647c8',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ElectricMemory.Name',
    display_name='Electric Memory',
    searchable_by=['Electric Memory', 'Pokémon Tool', 'ElectricMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=121,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Silvally-GX this card is attached to is a Lightning Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
