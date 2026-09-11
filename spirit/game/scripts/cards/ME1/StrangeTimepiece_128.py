from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="a9fda174-92be-5c3a-81c7-ce7eb789ea19",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeTimepiece.Name",
    display_name="Strange Timepiece",
    searchable_by=["Strange Timepiece", "Item", "StrangeTimepiece"],
    subtypes=["Item"],
    collector_number=128,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Devolve 1 of your evolved Psychic Pokémon by putting any number of Evolution cards on it into your hand. (That Pokémon can't evolve this turn.)"),
)
