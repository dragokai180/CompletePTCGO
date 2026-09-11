from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='efa04d27-1a71-5a98-a0d9-d7a99c2c6795',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MaxiesHiddenBallTrick.Name',
    display_name="Maxie's Hidden Ball Trick",
    searchable_by=["Maxie's Hidden Ball Trick", 'Supporter', 'MaxiesHiddenBallTrick'],
    subtypes=['Supporter'],
    collector_number=133,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only when it is the last card in your hand. Put a Fighting Pokémon from your discard pile onto your Bench. Then, draw 5 cards.'),
    condition=standard_trainer_condition('You can play this card only when it is the last card in your hand. Put a Fighting Pokémon from your discard pile onto your Bench. Then, draw 5 cards.'),
)
