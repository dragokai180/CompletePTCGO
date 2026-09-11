from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='b1b4db87-cec7-5c55-84e9-dc8425cca5ee',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MistyLorelei.Name',
    display_name='Misty & Lorelei',
    searchable_by=['Misty & Lorelei', 'Supporter', 'TAG TEAM', 'MistyLorelei'],
    subtypes=['Supporter', 'TAG TEAM'],
    collector_number=199,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. When you play this card, you may discard 5 other cards from your hand. If you do, during this turn, your Water Pokémon can use their GX attacks even if you have used your GX attack.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. When you play this card, you may discard 5 other cards from your hand. If you do, during this turn, your Water Pokémon can use their GX attacks even if you have used your GX attack.'),
)
