from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='54a7c071-836c-55d3-840c-e06814f569c5',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SabrinaBrycen.Name',
    display_name='Sabrina & Brycen',
    searchable_by=['Sabrina & Brycen', 'Supporter', 'TAG TEAM', 'SabrinaBrycen'],
    subtypes=['Supporter', 'TAG TEAM'],
    collector_number=246,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    effect=standard_trainer_effect('Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. When you play this card, you may discard 5 other cards from your hand. If you do, you may also search for up to 3 Pokémon of different types in this way.'),
    condition=standard_trainer_condition('Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck. When you play this card, you may discard 5 other cards from your hand. If you do, you may also search for up to 3 Pokémon of different types in this way.'),
)
