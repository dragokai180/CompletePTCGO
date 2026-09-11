from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="8d5e687d-fa0f-552f-95b8-387f3bdf819c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseGalette.Name",
    display_name="Lumiose Galette",
    searchable_by=["Lumiose Galette", "Item", "LumioseGalette"],
    subtypes=["Item"],
    collector_number=78,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Heal 20 damage and remove a Special Condition from your Active Pokémon."),
)
