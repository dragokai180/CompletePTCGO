from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='138ffcaa-5146-5450-8849-d9e4afb25a84',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BellelbaBrycenMan.Name',
    display_name='Bellelba & Brycen-Man',
    searchable_by=['Bellelba & Brycen-Man', 'Supporter', 'TAG TEAM', 'BellelbaBrycenMan'],
    subtypes=['Supporter', 'TAG TEAM'],
    collector_number=186,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard 3 cards from the top of each player's deck. When you play this card, you may discard 3 other cards from your hand. If you do, each player discards their Benched Pokémon until they have 3 Benched Pokémon. Your opponent discards first."),
    condition=standard_trainer_condition("Discard 3 cards from the top of each player's deck. When you play this card, you may discard 3 other cards from your hand. If you do, each player discards their Benched Pokémon until they have 3 Benched Pokémon. Your opponent discards first."),
)
