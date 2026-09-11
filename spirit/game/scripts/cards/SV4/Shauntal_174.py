from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9a6fd652-cd10-5b24-93f0-6b475dbde8c7',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Shauntal.Name',
    display_name='Shauntal',
    searchable_by=['Shauntal', 'Supporter', 'Shauntal'],
    subtypes=['Supporter'],
    collector_number=174,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot. If tails, switch your Active Pokémon with 1 of your Benched Pokémon."),
    condition=standard_trainer_condition("Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot. If tails, switch your Active Pokémon with 1 of your Benched Pokémon."),
)
