from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='d49d2326-52be-5d28-8d2b-60490845d287',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Jacq.Name',
    display_name='Jacq',
    searchable_by=['Jacq', 'Supporter', 'Jacq'],
    subtypes=['Supporter'],
    collector_number=175,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 Evolution Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 2 Evolution Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
