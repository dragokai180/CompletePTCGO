from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9031ea95-0e83-52a4-8287-7326fbda4a04',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BluesTactics.Name',
    display_name="Blue's Tactics",
    searchable_by=["Blue's Tactics", 'Supporter', 'BluesTactics'],
    subtypes=['Supporter'],
    collector_number=188,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('At the end of this turn, draw cards until you have 8 cards in your hand.'),
    condition=standard_trainer_condition('At the end of this turn, draw cards until you have 8 cards in your hand.'),
)
