from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = PokemonToolCardDef(
    guid='e84f90d5-a938-5154-88f4-da81bc050c73',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RockChestplate.Name',
    display_name='Rock Chestplate',
    searchable_by=['Rock Chestplate', 'Pokémon Tool', 'RockChestplate'],
    subtypes=['Pokémon Tool'],
    collector_number=192,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive("The Fighting Pokémon this card is attached to takes 30 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."),
)
