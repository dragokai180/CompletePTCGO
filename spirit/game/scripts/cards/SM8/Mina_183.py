from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='c94e3145-336b-5f21-b872-42b564179c00',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Mina.Name',
    display_name='Mina',
    searchable_by=['Mina', 'Supporter', 'Mina'],
    subtypes=['Supporter'],
    collector_number=183,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Fairy Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for a Fairy Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.'),
)
