from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='19b3fbda-0050-5089-b588-306b9114aec0',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Faba.Name',
    display_name='Faba',
    searchable_by=['Faba', 'Supporter', 'Faba'],
    subtypes=['Supporter'],
    collector_number=173,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Choose a Pokémon Tool or Special Energy card attached to 1 of your opponent's Pokémon, or any Stadium card in play, and put it in the Lost Zone."),
    condition=standard_trainer_condition("Choose a Pokémon Tool or Special Energy card attached to 1 of your opponent's Pokémon, or any Stadium card in play, and put it in the Lost Zone."),
)
