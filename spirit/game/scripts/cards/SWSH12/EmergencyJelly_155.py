from spirit.game.card_effects.trainers import EmergencyJellyPassive
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    passive=EmergencyJellyPassive(),
    guid="f87b4537-160d-59a5-b2a3-d82de56ae563",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmergencyJelly.Name",
    display_name="Emergency Jelly",
    searchable_by=["Emergency Jelly", "Item", "Pokémon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=155,
    set_code="SWSH12",
    rarity=Rarities.Uncommon
)
