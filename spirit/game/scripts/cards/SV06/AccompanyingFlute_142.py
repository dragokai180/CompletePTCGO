from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="6e44b374-a287-579d-b69c-4e98c4658a6b",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AccompanyingFlute.Name",
    display_name="Accompanying Flute",
    searchable_by=["Accompanying Flute", "Item", "AccompanyingFlute"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Reveal the top 5 cards of your opponent's deck. You may choose any number of Basic Pokémon you find there and put those Pokémon onto their Bench. Your opponent shuffles the other cards back into their deck."),
)
