from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='6bb1a280-76da-577b-a312-eba35a09cb8f',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name',
    display_name='Tate & Liza',
    searchable_by=['Tate & Liza', 'Supporter', 'TateLiza'],
    subtypes=['Supporter'],
    collector_number=148,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1:\n• Shuffle your hand into your deck then draw 5 cards.\n• Switch your Active Pokémon with 1 of your Benched Pokémon.'),
    condition=standard_trainer_condition('Choose 1:\n• Shuffle your hand into your deck then draw 5 cards.\n• Switch your Active Pokémon with 1 of your Benched Pokémon.'),
)
