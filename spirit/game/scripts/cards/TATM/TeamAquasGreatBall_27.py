from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='67503eb2-c932-5f2f-8aca-6f0c3aea29b6',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasGreatBall.Name',
    display_name="Team Aqua's Great Ball",
    searchable_by=["Team Aqua's Great Ball", 'Item', 'TeamAquasGreatBall'],
    subtypes=['Item'],
    collector_number=27,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Basic Team Aqua Pokémon and a basic Water Energy card, reveal them, and put them into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for a Basic Team Aqua Pokémon and a basic Water Energy card, reveal them, and put them into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
)
