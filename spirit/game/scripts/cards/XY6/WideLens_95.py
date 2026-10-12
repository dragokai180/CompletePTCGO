from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)
from spirit.game.card_effects.passives_common import BenchWeaknessResistancePassive


card = PokemonToolCardDef(
    guid='3fc2f08d-eca4-5445-917f-671123b7bfda',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.WideLens.Name',
    display_name='Wide Lens',
    searchable_by=['Wide Lens', 'Pokémon Tool', 'WideLens'],
    subtypes=['Pokémon Tool'],
    collector_number=95,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    passive=BenchWeaknessResistancePassive(),
)
