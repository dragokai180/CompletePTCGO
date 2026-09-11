from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import SilverMirrorPassive

card = PokemonToolCardDef(
    guid="197559bd-59fb-59d5-8bd9-3b68ef2693cf", key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilverMirror.Name",
    display_name="Silver Mirror", searchable_by=["Silver Mirror", "Pokémon Tool"],
    subtypes=["Pokémon Tool"], collector_number=89, set_code="BW10",
    rarity=Rarities.Uncommon, passive=SilverMirrorPassive(),
)
