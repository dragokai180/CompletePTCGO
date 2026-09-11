from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="5e00e3ac-c8b5-5203-87fd-4dfb7909cc65",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lucian.Name",
    display_name="Lucian",
    searchable_by=["Lucian", "Supporter", "Lucian"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Each player shuffles their hand and puts it on the bottom of their deck. If either player put any cards on the bottom of their deck in this way, each player flips a coin. If heads, that player draws 6 cards. If tails, they draw 3 cards."),
)
