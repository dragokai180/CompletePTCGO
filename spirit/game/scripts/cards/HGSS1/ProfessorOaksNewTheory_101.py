from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='96c6a5cc-e7b0-5c8b-bd0a-f63690b32aba',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksNewTheory.Name',
    display_name="Professor Oak's New Theory",
    searchable_by=["Professor Oak's New Theory", 'Supporter', 'ProfessorOaksNewTheory'],
    subtypes=['Supporter'],
    collector_number=101,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Shuffle your hand into your deck. Then, draw 6 cards.'),
    condition=standard_trainer_condition('You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card. Shuffle your hand into your deck. Then, draw 6 cards.'),
)
