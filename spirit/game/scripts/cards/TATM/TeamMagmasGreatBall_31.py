from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='489c8b1b-246c-590e-893e-14738017b7d6',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasGreatBall.Name',
    display_name="Team Magma's Great Ball",
    searchable_by=["Team Magma's Great Ball", 'Item', 'TeamMagmasGreatBall'],
    subtypes=['Item'],
    collector_number=31,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Basic Team Magma Pokémon and a basic Fighting Energy card, reveal them, and put them into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for a Basic Team Magma Pokémon and a basic Fighting Energy card, reveal them, and put them into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
)
