from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.standard_era import standard_passive


card = PokemonToolCardDef(
    guid="6a7b4b2f-2a34-53de-b5bd-6e328a88ef93",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SitrusBerry.Name",
    display_name="Sitrus Berry",
    searchable_by=["Sitrus Berry", "Pokémon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=182,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    passive=standard_passive("At the end of each turn, if the Pokémon this card is attached to has 3 or more damage counters on it, heal 30 damage from it and discard this card."),
)
