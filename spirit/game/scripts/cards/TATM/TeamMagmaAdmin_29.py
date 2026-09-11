from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='0a9d9923-ad43-56ca-9b2b-e2ffc812c8bc',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaAdmin.Name',
    display_name='Team Magma Admin',
    searchable_by=['Team Magma Admin', 'Supporter', 'TeamMagmaAdmin'],
    subtypes=['Supporter'],
    collector_number=29,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put up to 3 Team Magma Pokémon from your discard pile into your hand.'),
    condition=standard_trainer_condition('Put up to 3 Team Magma Pokémon from your discard pile into your hand.'),
)
