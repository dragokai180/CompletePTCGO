from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='de58d6a0-2a29-5daf-8613-9034f83579e3',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GrassMemory.Name',
    display_name='Grass Memory',
    searchable_by=['Grass Memory', 'Pokémon Tool', 'GrassMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=143,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Silvally-GX this card is attached to is a Grass Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
