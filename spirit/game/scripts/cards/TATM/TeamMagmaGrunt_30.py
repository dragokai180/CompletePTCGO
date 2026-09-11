from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='b70f88dd-ba84-5684-9ca6-03162b5b6181',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaGrunt.Name',
    display_name='Team Magma Grunt',
    searchable_by=['Team Magma Grunt', 'Supporter', 'TeamMagmaGrunt'],
    subtypes=['Supporter'],
    collector_number=30,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard a card from your hand. (If you can't discard a card, you can't play this card.) Draw 3 cards. If you discarded a Team Magma Pokémon, draw 1 more card."),
    condition=standard_trainer_condition("Discard a card from your hand. (If you can't discard a card, you can't play this card.) Draw 3 cards. If you discarded a Team Magma Pokémon, draw 1 more card."),
)
