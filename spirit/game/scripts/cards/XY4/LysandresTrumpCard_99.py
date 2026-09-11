from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='fe27cfa7-6c7a-5e28-bdf2-0f75f19b006d',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LysandresTrumpCard.Name',
    display_name="Lysandre's Trump Card",
    searchable_by=["Lysandre's Trump Card", 'Supporter', 'LysandresTrumpCard'],
    subtypes=['Supporter'],
    collector_number=99,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Each player shuffles all cards in his or her discard pile into his or her deck (except for Lysandre's Trump Card)."),
    condition=standard_trainer_condition("Each player shuffles all cards in his or her discard pile into his or her deck (except for Lysandre's Trump Card)."),
)
