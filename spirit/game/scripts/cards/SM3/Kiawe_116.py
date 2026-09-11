from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='be3ca5ba-43d8-5792-9d4c-6d4ea7da4d07',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name',
    display_name='Kiawe',
    searchable_by=['Kiawe', 'Supporter', 'Kiawe'],
    subtypes=['Supporter'],
    collector_number=116,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 4 Fire Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck. Your turn ends.'),
    condition=standard_trainer_condition('Search your deck for up to 4 Fire Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck. Your turn ends.'),
)
