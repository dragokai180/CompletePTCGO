from spirit.game.data_utils import StadiumCardDef, def_for
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive

DISPLAY_NAME = "Legendary Summit"


def _partner(board, player_id, card):
    """The other printing of Legendary Summit in hand, if any."""
    hand = board.find_player_area(player_id, "hand")
    for other in (hand.children if hand else []):
        if other.entity_id == card.entity_id:
            continue
        if other.archetype_id == card.archetype_id:
            continue
        definition = def_for(other.archetype_id)
        if getattr(definition, "display_name", None) == DISPLAY_NAME:
            return other
    return None


def _playable(board, player_id, card):
    """Needs a different printing of Legendary Summit in hand."""
    return _partner(board, player_id, card) is not None


class LegendarySummitPassive(Passive):
    """When a Colorless Pokémon is Knocked Out by damage from an opponent's
    attack, that opponent takes 1 fewer Prize card."""

    stacking_key = "LegendarySummit"

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.COLORLESS.value not in types:
            return count
        if not ctx.is_attack_effect() or ctx.attacker is None:
            return count
        if ctx.attacker.owning_player_id == pokemon.owning_player_id:
            return count
        if pokemon.entity_id not in ctx.attack_damage:
            return count
        return max(0, count - 1)


card = StadiumCardDef(
    guid="3a812f6f-3abf-5759-a9d1-db9cb0ac6911",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendarySummit.Name",
    display_name=DISPLAY_NAME,
    searchable_by=["Legendary Summit","Stadium","LegendarySummit"],
    subtypes=["Stadium"],
    collector_number=73,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_playable,
    companion=_partner,
    passive=LegendarySummitPassive(),
)
