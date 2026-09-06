from spirit.game.data_utils import StadiumCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_free_when


def _is_ns_pokemon(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("N's ")


card = StadiumCardDef(
    guid="d375bd53-88c9-5764-9272-0a67b123d4f9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsCastle.Name",
    display_name="N's Castle",
    searchable_by=["N's Castle", "Stadium", "NsCastle"],
    subtypes=["Stadium"],
    collector_number=152,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=retreat_free_when(lambda p, c: _is_ns_pokemon(p)),
)
