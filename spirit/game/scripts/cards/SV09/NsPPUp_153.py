from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_ns_pokemon(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("N's ")


def _is_benched_ns(pokemon) -> bool:
    return _is_ns_pokemon(pokemon) and not is_in_active_spot(pokemon)


def ns_pp_up_condition(board, player_id):
    if not requires_discard(is_basic_energy_card)(board, player_id):
        return False
    return any(_is_benched_ns(p) for p in board.pokemon_in_play(player_id))


card = ItemCardDef(
    guid="a66d34b1-ce65-53d9-938c-1c8176a55a94",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsPPUp.Name",
    display_name="N's PP Up",
    searchable_by=["N's PP Up", "Item", "NsPPUp"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=ns_pp_up_condition,
    effect=attach_from_discard(
        predicate=is_basic_energy_card,
        count=1,
        target=_is_benched_ns,
        prompt="Choose a Basic Energy card to attach.",
    ),
)
