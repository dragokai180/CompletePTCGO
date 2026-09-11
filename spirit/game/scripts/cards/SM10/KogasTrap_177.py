from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='fe0d8b54-8354-5e00-b2bc-14ee250a1450',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name',
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", 'Supporter', 'KogasTrap'],
    subtypes=['Supporter'],
    collector_number=177,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent's Active Pokémon is now Confused and Poisoned."),
    condition=standard_trainer_condition("Your opponent's Active Pokémon is now Confused and Poisoned."),
)
