from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="f0b0a90e-e6c5-55ac-945a-8c6e7f60e836",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BoxedOrder.Name",
    display_name="Boxed Order",
    searchable_by=["Boxed Order", "Item", "BoxedOrder"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Then, shuffle your deck. Your turn ends."),
)
