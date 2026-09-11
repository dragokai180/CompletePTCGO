from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="96a89aba-bd99-5fec-ac6e-f28de7f95273",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegatonBlower.Name",
    display_name="Megaton Blower",
    searchable_by=["Megaton Blower", "Item", "ACE SPEC", "MegatonBlower"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=182,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=standard_trainer_effect("Discard all Pokémon Tools and Special Energy from all of your opponent's Pokémon, and discard a Stadium in play. ACE SPEC: You can't have more than 1 ACE SPEC card in your deck."),
)
