from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='ece2a15c-9062-5922-b9fb-3b4124fcd1fb',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name',
    display_name='Evelyn',
    searchable_by=['Evelyn', 'Supporter', 'Evelyn'],
    subtypes=['Supporter'],
    collector_number=141,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can play this card only if your opponent's Active Pokémon is a Stage 1 Pokémon. Draw 4 cards."),
    condition=standard_trainer_condition("You can play this card only if your opponent's Active Pokémon is a Stage 1 Pokémon. Draw 4 cards."),
)
