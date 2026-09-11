from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="2fbdb90b-a0ef-5d6c-822e-3aeee11b7e8e",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HopsBag.Name",
    display_name="Hop's Bag",
    searchable_by=["Hop's Bag", "Item", "HopsBag"],
    subtypes=["Item"],
    collector_number=147,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for up to 2 Basic Hop's Pokémon and put them onto your Bench. Then, shuffle your deck."),
)
