from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.standard_era import standard_passive


card = PokemonToolCardDef(
    guid="fea6a9ac-0258-56e1-8696-2186eb91ea09",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumBerry.Name",
    display_name="Lum Berry",
    searchable_by=["Lum Berry", "Pokémon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=168,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    passive=standard_passive("At the end of each turn, if the Pokémon this card is attached to is affected by any Special Conditions, it recovers from all of them, and discard this card."),
)
