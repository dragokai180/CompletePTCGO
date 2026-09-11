from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="78a2208c-763c-590b-b237-f1f40022bcb1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brassius.Name",
    display_name="Brassius",
    searchable_by=["Brassius", "Supporter", "Brassius"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=standard_trainer_effect("Count the cards in your hand, shuffle those cards into your deck, then draw that many cards plus 1."),
)
