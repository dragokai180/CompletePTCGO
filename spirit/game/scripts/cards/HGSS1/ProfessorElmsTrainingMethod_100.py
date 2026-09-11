from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='af50690d-42dc-5b00-b59c-d33aad08c347',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name',
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", 'Supporter', 'ProfessorElmsTrainingMethod'],
    subtypes=['Supporter'],
    collector_number=100,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
)
