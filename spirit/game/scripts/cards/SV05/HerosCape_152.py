from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool

card = PokemonToolCardDef(
    guid="8a266173-abb9-5670-88d2-b87d75e44b29",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HerosCape.Name",
    display_name="Hero's Cape",
    searchable_by=["Hero's Cape", "Item", "Pokémon Tool", "ACE SPEC", "HerosCape"],
    subtypes=["Item", "Pokémon Tool", "ACE SPEC"],
    collector_number=152,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareUltra,
    passive=hp_bonus_tool(100),
)
