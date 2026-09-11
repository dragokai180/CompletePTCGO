from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = ItemCardDef(
    guid="7ef29643-8712-5a65-91da-d74c087985c9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedeemableTicket.Name",
    display_name="Redeemable Ticket",
    searchable_by=["Redeemable Ticket", "Item", "RedeemableTicket"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Count your Prize cards, shuffle them, and put them on the bottom of your deck. Then, take that many cards from the top of your deck and put them face down as your Prize cards."),
)
