from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='f7b0941e-0a4d-5f1f-a46f-78a5f6b1467e',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name',
    display_name='Dana',
    searchable_by=['Dana', 'Supporter', 'Dana'],
    subtypes=['Supporter'],
    collector_number=137,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if your opponent's Active Pokémon is a Stage 2 Pokémon. Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck."),
    condition=standard_trainer_condition("You can play this card only if your opponent's Active Pokémon is a Stage 2 Pokémon. Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck."),
)
