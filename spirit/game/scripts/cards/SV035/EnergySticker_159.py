from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ea8928ab-6e2c-522b-9385-f69a2d3471a3',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergySticker.Name',
    display_name='Energy Sticker',
    searchable_by=['Energy Sticker', 'Item', 'EnergySticker'],
    subtypes=['Item'],
    collector_number=159,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, attach a Basic Energy card from your discard pile to 1 of your Benched Pokémon.'),
    condition=standard_trainer_condition('Flip a coin. If heads, attach a Basic Energy card from your discard pile to 1 of your Benched Pokémon.'),
)
