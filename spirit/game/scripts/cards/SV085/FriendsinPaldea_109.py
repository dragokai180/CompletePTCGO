from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="599681c6-6058-565b-8daa-5ae181b09a1c",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinPaldea.Name",
    display_name="Friends in Paldea",
    searchable_by=["Friends in Paldea", "Supporter", "FriendsinPaldea"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Draw 3 cards."),
)
