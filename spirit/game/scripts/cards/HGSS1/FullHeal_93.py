from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='d9f4c6af-2405-5c90-85ba-050a39590caf',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name',
    display_name='Full Heal',
    searchable_by=['Full Heal', 'Item', 'FullHeal'],
    subtypes=['Item'],
    collector_number=93,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Remove all Special Conditions from your Active Pokémon.'),
    condition=standard_trainer_condition('Remove all Special Conditions from your Active Pokémon.'),
)
