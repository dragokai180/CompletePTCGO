from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="2eb5ba3a-6e28-56af-a897-a3059b45f176",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwatter.Name",
    display_name="Energy Swatter",
    searchable_by=["Energy Swatter", "Item", "EnergySwatter"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent reveals their hand, and you choose an Energy card you find there and put it on the bottom of their deck."),
)
