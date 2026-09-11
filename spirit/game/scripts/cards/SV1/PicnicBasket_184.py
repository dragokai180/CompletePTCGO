from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='9bec5e9a-9517-5731-9913-908829d4d8b3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PicnicBasket.Name',
    display_name='Picnic Basket',
    searchable_by=['Picnic Basket', 'Item', 'PicnicBasket'],
    subtypes=['Item'],
    collector_number=184,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Heal 30 damage from each Pokémon (both yours and your opponent's)."),
    condition=standard_trainer_condition("Heal 30 damage from each Pokémon (both yours and your opponent's)."),
)
