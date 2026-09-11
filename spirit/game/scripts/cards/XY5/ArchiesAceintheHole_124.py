from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='5e2efbe1-2f95-58b8-b68e-9bdea3db53d2',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ArchiesAceintheHole.Name',
    display_name="Archie's Ace in the Hole",
    searchable_by=["Archie's Ace in the Hole", 'Supporter', 'ArchiesAceintheHole'],
    subtypes=['Supporter'],
    collector_number=124,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only when it is the last card in your hand. Put a Water Pokémon from your discard pile onto your Bench. Then, draw 5 cards.'),
    condition=standard_trainer_condition('You can play this card only when it is the last card in your hand. Put a Water Pokémon from your discard pile onto your Bench. Then, draw 5 cards.'),
)
