from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="aafc5c57-26c6-529b-aae7-003924485dbe",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillyONare.Name",
    display_name="Billy & O'Nare",
    searchable_by=["Billy & O'Nare", "Supporter", "BillyONare"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Draw 2 cards. Then, if you have 10 or more cards in your hand, draw 2 more cards."),
)
