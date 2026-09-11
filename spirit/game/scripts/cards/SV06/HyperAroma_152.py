from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="885ca228-2ea5-58f7-8ed2-c6be13fd8501",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperAroma.Name",
    display_name="Hyper Aroma",
    searchable_by=["Hyper Aroma", "Item", "ACE SPEC", "HyperAroma"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=152,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("You can't have more than 1 ACE SPEC card in your deck. Search your deck for up to 3 Stage 1 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
