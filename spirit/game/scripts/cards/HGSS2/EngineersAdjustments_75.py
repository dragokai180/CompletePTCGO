from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5a405e6b-190c-56bc-8893-eede555efb01',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EngineersAdjustments.Name',
    display_name="Engineer's Adjustments",
    searchable_by=["Engineer's Adjustments", 'Supporter', 'EngineersAdjustments'],
    subtypes=['Supporter'],
    collector_number=75,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Discard an Energy card from your hand. Then, draw 4 cards.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Discard an Energy card from your hand. Then, draw 4 cards.'),
)
