from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='10f4d65a-b3c7-57ce-88f6-31ad0bc0f4d9',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MistysFavor.Name',
    display_name="Misty's Favor",
    searchable_by=["Misty's Favor", 'Supporter', 'MistysFavor'],
    subtypes=['Supporter'],
    collector_number=202,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 3 Supporter cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Supporter cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
