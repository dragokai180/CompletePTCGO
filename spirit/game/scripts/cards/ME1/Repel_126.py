from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="20cb2f33-aecf-515c-9814-de3290e3e5d0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Repel.Name",
    display_name="Repel",
    searchable_by=["Repel", "Item", "Repel"],
    subtypes=["Item"],
    collector_number=126,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)"),
)
