from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='0697d68b-a1f8-5182-bc75-290b5d6428f6',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CoachTrainer.Name',
    display_name='Coach Trainer',
    searchable_by=['Coach Trainer', 'Supporter', 'CoachTrainer'],
    subtypes=['Supporter'],
    collector_number=192,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 2 cards. If your Active Pokémon is a TAG TEAM Pokémon, draw 2 more cards.'),
    condition=standard_trainer_condition('Draw 2 cards. If your Active Pokémon is a TAG TEAM Pokémon, draw 2 more cards.'),
)
