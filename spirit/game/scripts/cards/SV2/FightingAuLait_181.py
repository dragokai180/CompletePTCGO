from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='1699f16d-7256-5025-bee2-eff52776d239',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FightingAuLait.Name',
    display_name='Fighting Au Lait',
    searchable_by=['Fighting Au Lait', 'Item', 'FightingAuLait'],
    subtypes=['Item'],
    collector_number=181,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can use this card only if you have more Prize cards remaining than your opponent.Heal 60 damage from 1 of your Pokémon.'),
    condition=standard_trainer_condition('You can use this card only if you have more Prize cards remaining than your opponent.Heal 60 damage from 1 of your Pokémon.'),
)
