from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="83b7dccb-b2e3-54d9-9c03-d0ae542b3f5b",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drasna.Name",
    display_name="Drasna",
    searchable_by=["Drasna", "Supporter", "Drasna"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Shuffle your hand into your deck. Then, flip a coin. If heads, draw 8 cards. If tails, draw 3 cards."),
)
