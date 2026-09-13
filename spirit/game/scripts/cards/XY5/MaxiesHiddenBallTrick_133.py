from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.trainer_followup import last_card_recovery
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


_effect, _condition = last_card_recovery(PokemonTypes.FIGHTING.value)

card = SupporterCardDef(
    guid='efa04d27-1a71-5a98-a0d9-d7a99c2c6795',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MaxiesHiddenBallTrick.Name',
    display_name="Maxie's Hidden Ball Trick",
    searchable_by=["Maxie's Hidden Ball Trick", 'Supporter', 'MaxiesHiddenBallTrick'],
    subtypes=['Supporter'],
    collector_number=133,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=_effect,
    condition=_condition,
)
