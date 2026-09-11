from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="869d30d1-42b1-52f9-bc65-3f56380fff9d",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caretaker.Name",
    display_name="Caretaker",
    searchable_by=["Caretaker", "Supporter", "Caretaker"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Draw 2 cards. If you drew any cards in this way and if Community Center is in play, shuffle this Caretaker into your deck instead of discarding it."),
)
