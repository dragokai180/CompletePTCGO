from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="2378f35e-224b-53df-957c-37e5c81a81c0",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousLaser.Name",
    display_name="Dangerous Laser",
    searchable_by=["Dangerous Laser", "Item", "ACE SPEC", "DangerousLaser"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=58,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("You can't have more than 1 ACE SPEC card in your deck. Your opponent's Active Pokémon is now Burned and Confused."),
)
