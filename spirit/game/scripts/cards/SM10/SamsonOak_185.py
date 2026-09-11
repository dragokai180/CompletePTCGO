from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='23e345e9-9e38-5bdd-8e07-46ddf59d6d1e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SamsonOak.Name',
    display_name='Samson Oak',
    searchable_by=['Samson Oak', 'Supporter', 'SamsonOak'],
    subtypes=['Supporter'],
    collector_number=185,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Draw 2 cards. If both Active Pokémon are the same type, draw 2 more cards.'),
    condition=standard_trainer_condition('Draw 2 cards. If both Active Pokémon are the same type, draw 2 more cards.'),
)
