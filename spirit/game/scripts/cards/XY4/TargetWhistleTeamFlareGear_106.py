from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='2ba5e8c2-2986-59c8-936b-af875bdf0431',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TargetWhistleTeamFlareGear.Name',
    display_name='Target Whistle Team Flare Gear',
    searchable_by=['Target Whistle Team Flare Gear', 'Item', 'TargetWhistleTeamFlareGear'],
    subtypes=['Item'],
    collector_number=106,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put a Basic Pokémon from your opponent's discard pile onto his or her Bench. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Put a Basic Pokémon from your opponent's discard pile onto his or her Bench. You may play as many Item cards as you like during your turn (before your attack)."),
)
