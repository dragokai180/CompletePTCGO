from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="6f7f0ce2-0e9d-5a38-97ff-94359cf21074",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassiopeia.Name",
    display_name="Cassiopeia",
    searchable_by=["Cassiopeia", "Supporter", "Cassiopeia"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only when it is the last card in your hand.  Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck."),
)
