from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="dbdae281-8841-5859-9c77-82b5b87ac662",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kofu.Name",
    display_name="Kofu",
    searchable_by=["Kofu", "Supporter", "Kofu"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put 2 cards from your hand on the bottom of your deck in any order. If you put 2 cards on the bottom of your deck in this way, draw 4 cards. (If you can't put 2 cards from your hand on the bottom of your deck, you can't use this card.)"),
)
