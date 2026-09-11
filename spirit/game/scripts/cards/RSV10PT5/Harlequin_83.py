from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="cfd6cc68-b88a-5c53-be51-296535cb92b7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Harlequin.Name",
    display_name="Harlequin",
    searchable_by=["Harlequin", "Supporter", "Harlequin"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Each player shuffles their hand into their deck. Then, flip a coin. If heads, you draw 5 cards, and your opponent draws 3 cards. If tails, you draw 3 cards, and your opponent draws 5 cards."),
)
