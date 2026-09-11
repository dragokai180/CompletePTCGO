from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='6d4713e6-8061-5b33-b82b-7c09ba157c49',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaAdmin.Name',
    display_name='Team Aqua Admin',
    searchable_by=['Team Aqua Admin', 'Supporter', 'TeamAquaAdmin'],
    subtypes=['Supporter'],
    collector_number=25,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach a basic Energy card from your discard pile to your Active Team Aqua Pokémon.'),
    condition=standard_trainer_condition('Attach a basic Energy card from your discard pile to your Active Team Aqua Pokémon.'),
)
