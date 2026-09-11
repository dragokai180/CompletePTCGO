from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="0730eece-5e4c-5ffa-a146-bd70b579fb2b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Waitress.Name",
    display_name="Waitress",
    searchable_by=["Waitress", "Supporter", "Waitress"],
    subtypes=["Supporter"],
    collector_number=215,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Look at the top 6 cards of your deck and attach a Basic Energy card you find there to 1 of your Pokémon. Shuffle the other cards back into your deck."),
)
