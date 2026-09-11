from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9dc70b74-7f48-5ba3-86c1-3825999fb295',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Geeta.Name',
    display_name='Geeta',
    searchable_by=['Geeta', 'Supporter', 'Geeta'],
    subtypes=['Supporter'],
    collector_number=188,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    effect=standard_trainer_effect("Search your deck for up to 2 Basic Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck. During this turn, your Pokémon can't attack. (This includes Pokémon that come into play this turn.)"),
    condition=standard_trainer_condition("Search your deck for up to 2 Basic Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck. During this turn, your Pokémon can't attack. (This includes Pokémon that come into play this turn.)"),
)
