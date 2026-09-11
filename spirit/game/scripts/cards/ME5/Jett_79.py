from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="d0e13667-4c6c-52ca-9f05-777367508a3f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jett.Name",
    display_name="Jett",
    searchable_by=["Jett", "Supporter", "Jett"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw a card for each of your opponent's Mega Evolution Pokémon ex in play."),
)
