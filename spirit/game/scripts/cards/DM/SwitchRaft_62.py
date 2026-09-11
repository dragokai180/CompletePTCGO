from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='09cc0b2d-be04-5aa3-804c-e300eb45ab0c',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name',
    display_name='Switch Raft',
    searchable_by=['Switch Raft', 'Item', 'SwitchRaft'],
    subtypes=['Item'],
    collector_number=62,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Switch your Active Water Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Switch your Active Water Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench. You may play as many Item cards as you like during your turn (before your attack).'),
)
