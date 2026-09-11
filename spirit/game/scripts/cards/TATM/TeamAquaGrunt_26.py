from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='8f7dd117-d369-5ae5-8de7-598a8da25c9c',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaGrunt.Name',
    display_name='Team Aqua Grunt',
    searchable_by=['Team Aqua Grunt', 'Supporter', 'TeamAquaGrunt'],
    subtypes=['Supporter'],
    collector_number=26,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard a card from your hand. (If you can't discard a card, you can't play this card.) Draw 3 cards. If you discarded a Team Aqua Pokémon, draw 1 more card."),
    condition=standard_trainer_condition("Discard a card from your hand. (If you can't discard a card, you can't play this card.) Draw 3 cards. If you discarded a Team Aqua Pokémon, draw 1 more card."),
)
