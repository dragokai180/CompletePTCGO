from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='fdd971e0-c437-596c-a49a-0a92d7b95d86',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name',
    display_name='Guzma & Hala',
    searchable_by=['Guzma & Hala', 'Supporter', 'TAG TEAM', 'GuzmaHala'],
    subtypes=['Supporter', 'TAG TEAM'],
    collector_number=193,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck. When you play this card, you may discard 2 other cards from your hand. If you do, you may also search for a Pokémon Tool card and a Special Energy card in this way.'),
    condition=standard_trainer_condition('Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck. When you play this card, you may discard 2 other cards from your hand. If you do, you may also search for a Pokémon Tool card and a Special Energy card in this way.'),
)
