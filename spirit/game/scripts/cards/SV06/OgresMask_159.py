from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="9b6f02b8-d187-5fed-bb34-7ce8d014361f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OgresMask.Name",
    display_name="Ogre's Mask",
    searchable_by=["Ogre's Mask", "Item", "OgresMask"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Choose a Pokémon ex in your discard pile that has \"Ogerpon\" in its name, and switch it with 1 of your Pokémon ex in play that has \"Ogerpon\" in its name. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon."),
)
