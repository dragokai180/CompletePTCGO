from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="9c6f88bb-eba2-5df1-bfe1-9c57cba6c010",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EthansAdventure.Name",
    display_name="Ethan's Adventure",
    searchable_by=["Ethan's Adventure", "Supporter", "EthansAdventure"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Search your deck for up to 3 in any combination of Ethan's Pokémon and Basic Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck."),
)
