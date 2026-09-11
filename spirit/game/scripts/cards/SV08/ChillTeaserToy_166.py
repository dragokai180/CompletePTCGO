from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="48c8af8d-88a8-5fe6-8301-fa6a17f91474",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChillTeaserToy.Name",
    display_name="Chill Teaser Toy",
    searchable_by=["Chill Teaser Toy", "Item", "ChillTeaserToy"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you go second, and only during your first turn.  Put an Energy attached to 1 of your opponent's Pokémon into their hand."),
)
