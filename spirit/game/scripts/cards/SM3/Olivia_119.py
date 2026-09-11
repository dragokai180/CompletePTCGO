from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='0653276e-fc3a-57d1-990a-2fef3e5126cd',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Olivia.Name',
    display_name='Olivia',
    searchable_by=['Olivia', 'Supporter', 'Olivia'],
    subtypes=['Supporter'],
    collector_number=119,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 Pokémon-GX, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 2 Pokémon-GX, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
