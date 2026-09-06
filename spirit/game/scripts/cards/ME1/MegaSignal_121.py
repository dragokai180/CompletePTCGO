from spirit.game.data_utils import ItemCardDef, is_pokemon_ex, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand


def _is_mega_evolution_ex(card):
    return "SV_Mega" in subtypes_for(card.archetype_id) and is_pokemon_ex(card.archetype_id)


card = ItemCardDef(
    guid="fa70ef3e-1626-5313-8467-278e0072161a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaSignal.Name",
    display_name="Mega Signal",
    searchable_by=["Mega Signal","Item","MegaSignal"],
    subtypes=["Item"],
    collector_number=121,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _is_mega_evolution_ex, count=1, minimum=0, reveal=True,
        prompt="Choose a Mega Evolution Pokémon ex to put into your hand.",
    ),
)
