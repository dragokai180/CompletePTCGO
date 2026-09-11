from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='06a476f5-5dbe-54e5-9687-eeaf9c1f71c5',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Olympia.Name',
    display_name='Olympia',
    searchable_by=['Olympia', 'Supporter', 'Olympia'],
    subtypes=['Supporter'],
    collector_number=66,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Switch your Active Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench.'),
    condition=standard_trainer_condition('Switch your Active Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench.'),
)
