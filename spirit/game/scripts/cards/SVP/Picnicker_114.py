from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="0138d62e-0067-5835-aebe-9d04704ab6f3",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Picnicker.Name",
    display_name="Picnicker",
    searchable_by=["Picnicker", "Supporter", "Picnicker"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    effect=standard_trainer_effect("Flip a coin. If heads, draw 4 cards. If tails, draw 2 cards."),
)
