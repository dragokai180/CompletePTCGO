from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="884e5682-2c6d-5d70-b50a-b25185ee311b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesBargain.Name",
    display_name="Lt. Surge's Bargain",
    searchable_by=["Lt. Surge's Bargain", "Supporter", "LtSurgesBargain"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Ask your opponent if each player may take a Prize card. If yes, each player takes a Prize card. If no, you draw 4 cards."),
)
