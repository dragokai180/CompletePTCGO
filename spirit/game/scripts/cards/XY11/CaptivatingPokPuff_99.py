from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='7ca0fb60-d5de-56ff-81e8-3553f6412d94',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CaptivatingPokPuff.Name',
    display_name='Captivating Poké Puff',
    searchable_by=['Captivating Poké Puff', 'Item', 'CaptivatingPokPuff'],
    subtypes=['Item'],
    collector_number=99,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent reveals his or her hand. Put any number of Basic Pokémon you find there onto your opponent's Bench. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Your opponent reveals his or her hand. Put any number of Basic Pokémon you find there onto your opponent's Bench. You may play as many Item cards as you like during your turn (before your attack)."),
)
