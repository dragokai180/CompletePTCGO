from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='1a0fdbbf-214e-501e-ba70-8d97fc3f623b',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LostRemover.Name',
    display_name='Lost Remover',
    searchable_by=['Lost Remover', 'Item', 'LostRemover'],
    subtypes=['Item'],
    collector_number=80,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put 1 Special Energy card attached to 1 of your opponent's Pokémon in the Lost Zone."),
    condition=standard_trainer_condition("Put 1 Special Energy card attached to 1 of your opponent's Pokémon in the Lost Zone."),
)
