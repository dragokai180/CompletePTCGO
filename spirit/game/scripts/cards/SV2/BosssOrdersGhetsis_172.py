from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='cdfd3d77-a42f-5e0b-b988-00f195eba9ad',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BosssOrdersGhetsis.Name',
    display_name="Boss's Orders (Ghetsis)",
    searchable_by=["Boss's Orders (Ghetsis)", 'Supporter', 'BosssOrdersGhetsis'],
    subtypes=['Supporter'],
    collector_number=172,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    effect=standard_trainer_effect("Switch in 1 of your opponent's Benched Pokémon to the Active Spot."),
    condition=standard_trainer_condition("Switch in 1 of your opponent's Benched Pokémon to the Active Spot."),
)
