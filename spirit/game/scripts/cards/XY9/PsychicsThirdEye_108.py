from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c0c48f4f-0d69-5b91-af3f-1f25caf3e771',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PsychicsThirdEye.Name',
    display_name="Psychic's Third Eye",
    searchable_by=["Psychic's Third Eye", 'Supporter', 'PsychicsThirdEye'],
    subtypes=['Supporter'],
    collector_number=108,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals his or her hand. Discard as many cards as you like from your hand. Then, draw that many cards.'),
    condition=standard_trainer_condition('Your opponent reveals his or her hand. Discard as many cards as you like from your hand. Then, draw that many cards.'),
)
