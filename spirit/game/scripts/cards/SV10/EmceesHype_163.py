from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="42eb239f-2e2c-562f-a5ac-8996fc7f4667",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmceesHype.Name",
    display_name="Emcee's Hype",
    searchable_by=["Emcee's Hype", "Supporter", "EmceesHype"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Draw 2 cards. If your opponent has 3 or fewer Prize cards remaining, draw 2 more cards."),
)
