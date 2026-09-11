from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='bb508993-d0c7-55a3-9634-bbcb2834f7b1',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WaterMemory.Name',
    display_name='Water Memory',
    searchable_by=['Water Memory', 'Pokémon Tool', 'WaterMemory'],
    subtypes=['Pokémon Tool'],
    collector_number=157,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Silvally-GX this card is attached to is a Water Pokémon. You may play as many Item cards as you like during your turn (before your attack).'),
)
