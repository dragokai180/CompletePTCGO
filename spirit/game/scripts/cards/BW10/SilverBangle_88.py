from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import SilverBanglePassive

card = PokemonToolCardDef(
    guid="f0764808-e7cd-5ea8-a523-d3a27a41581a", key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilverBangle.Name",
    display_name="Silver Bangle", searchable_by=["Silver Bangle", "Pokémon Tool"],
    subtypes=["Pokémon Tool"], collector_number=88, set_code="BW10",
    rarity=Rarities.Uncommon, passive=SilverBanglePassive(),
)
