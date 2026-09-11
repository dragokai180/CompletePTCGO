from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="334ba6be-b93f-5519-8b7a-6c6fc1746d06",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearchPro.Name",
    display_name="Energy Search Pro",
    searchable_by=["Energy Search Pro", "Item", "ACE SPEC", "EnergySearchPro"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=176,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("Search your deck for any number of Basic Energy cards of different types, reveal them, and put them into your hand. Then, shuffle your deck. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
