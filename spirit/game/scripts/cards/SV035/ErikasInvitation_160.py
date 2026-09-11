from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='1fdd21cb-42ef-50ac-8c2c-4cbb34b65f55',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ErikasInvitation.Name',
    display_name="Erika's Invitation",
    searchable_by=["Erika's Invitation", 'Supporter', 'ErikasInvitation'],
    subtypes=['Supporter'],
    collector_number=160,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent reveals their hand, and you put a Basic Pokémon you find there onto your opponent's Bench. If you put a Pokémon onto their Bench in this way, switch in that Pokémon to the Active Spot."),
    condition=standard_trainer_condition("Your opponent reveals their hand, and you put a Basic Pokémon you find there onto your opponent's Bench. If you put a Pokémon onto their Bench in this way, switch in that Pokémon to the Active Spot."),
)
