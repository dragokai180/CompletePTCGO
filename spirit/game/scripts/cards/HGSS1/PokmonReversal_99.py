from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='4eef2063-1115-58f7-932d-836a9e398199',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonReversal.Name',
    display_name='Pokémon Reversal',
    searchable_by=['Pokémon Reversal', 'Item', 'PokmonReversal'],
    subtypes=['Item'],
    collector_number=99,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Flip a coin. If heads, choose 1 of your opponent's Benched Pokémon, and switch it with your opponent's Active Pokémon."),
    condition=standard_trainer_condition("Flip a coin. If heads, choose 1 of your opponent's Benched Pokémon, and switch it with your opponent's Active Pokémon."),
)
