from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1a44fea6-e882-53b6-be66-799e0c629b48',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LasssSpecial.Name',
    display_name="Lass's Special",
    searchable_by=["Lass's Special", 'Supporter', 'LasssSpecial'],
    subtypes=['Supporter'],
    collector_number=103,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw a card for each of your opponent's Benched Basic Pokémon."),
    condition=standard_trainer_condition("Draw a card for each of your opponent's Benched Basic Pokémon."),
)
