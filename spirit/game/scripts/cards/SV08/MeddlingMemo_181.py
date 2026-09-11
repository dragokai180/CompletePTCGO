from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="7c99bdd3-7cc1-538d-8ec0-4e1019fc843c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MeddlingMemo.Name",
    display_name="Meddling Memo",
    searchable_by=["Meddling Memo", "Item", "MeddlingMemo"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent counts the cards in their hand, shuffles those cards, and puts them on the bottom of their deck. If they do, they draw that many cards."),
)
