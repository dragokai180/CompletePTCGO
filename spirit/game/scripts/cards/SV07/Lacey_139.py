from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="1d073d90-7fc1-5f41-82a4-7a809a57eb43",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter", "Lacey"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Shuffle your hand into your deck. Then, draw 4 cards. If your opponent has 3 or fewer Prize cards remaining, draw 8 cards instead."),
)
