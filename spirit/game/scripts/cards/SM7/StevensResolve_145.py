from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='e274e0be-74d8-58c2-b796-9200f85d3341',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name',
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", 'Supporter', 'StevensResolve'],
    subtypes=['Supporter'],
    collector_number=145,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    effect=standard_trainer_effect('Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck. Your turn ends.'),
    condition=standard_trainer_condition('Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck. Your turn ends.'),
)
