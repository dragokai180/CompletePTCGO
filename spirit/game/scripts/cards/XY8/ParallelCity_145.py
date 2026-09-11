"""Parallel City (XY - BREAKthrough 145/162).

  "Choose which way this card faces before you play it.
   This (down) player can't have more than 3 Benched Pokemon. (When this
   card comes into play, this (down) player discards Benched Pokemon until
   he or she has 3 Pokemon on the Bench.)
   Any damage done by attacks from this (down) player's Grass, Fire, or
   Water Pokemon is reduced by 20 (before applying Weakness and
   Resistance)."

Two halves, one facing each player: whoever plays it picks which side gets
which. The orientation is asked for in the Stadium's `effect` -- the hook
_execute_play_stadium runs after the card is on the board and before
enforce_bench_capacity(), which is exactly the window this card needs: the
answer decides whose Bench the shrink applies to, and the shrink then
happens on its own.

  the Bench half   bench_capacity returns 3 for the chosen side only, the
                   way Sudowoodo caps the opponent. effective_bench_capacity
                   takes the smallest override, and the "discards until 3"
                   clause is just enforce_bench_capacity doing its usual job.
  the damage half  modify_damage_dealt, which runs before weakness and
                   resistance (Muscle Band relies on the same ordering).
                   No is_opposing filter: the card says "any damage done by
                   attacks", not "damage to the Defending Pokemon".

The chosen side lives in the card-orientation attribute sent to the native
client renderer. Normal orientation points the damage-reduction half at the
owner and the Bench-limit half at the opponent; inverted swaps them.

Nothing on the playmat says which half landed on whom (see the note on the
status rows below), but the printed card carries both texts -- one of them
upside down -- so the picture in the Stadium slot shows the whole card either
way. The client does have a CardOrientations.Inverted for flipping the art,
but the attribute that drives it is not mapped here.
"""

from typing import Optional

from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.models.board import PlayerEntity
from spirit.game.session.passives import Passive

# The LocalizationDB still ships this card's per-player status text
# (specialvisualizations.player.xy8_145.parallelcitya / .parallelcityb), but
# nothing in pie-src.dll references it: there is no ParallelCity identifier and
# no "specialvisualizations.player" literal anywhere in the assembly. Pushing
# rows with those names as the displayType threw NullReferenceException inside
# the client's sequence handling -- displayType has to be a real
# VisualizationTypes member (the client derefs the parsed enum unguarded), and
# neither name is one. So this card contributes no status rows; both halves
# still apply, they are just not annotated on the playmat.

_REDUCED_TYPES = (
    PokemonTypes.GRASS.value, PokemonTypes.FIRE.value, PokemonTypes.WATER.value,
)

def _player_ids(carrier):
    """Both players, read off the playmat the Stadium sits on (Stadium ->
    activeStadium -> playmat), the same walk Area Zero Underdepths uses."""
    playmat = carrier.parent.parent if carrier.parent else None
    if playmat is None:
        return []
    return [
        child.owning_player_id for child in playmat.children
        if isinstance(child, PlayerEntity) and child.owning_player_id
    ]


def bench_side(carrier) -> Optional[str]:
    """The player whose Bench is capped; the other player takes the -20."""
    owner = getattr(carrier, "owning_player_id", None)
    if owner is None:
        return None
    opponent = next((p for p in _player_ids(carrier) if p != owner), None)
    inverted = carrier.get_attribute(AttrID.CARD_ORIENTATION, 0) == 1
    return owner if inverted else opponent


def _damage_side(carrier) -> Optional[str]:
    bench = bench_side(carrier)
    if bench is None:
        return None
    return next((p for p in _player_ids(carrier) if p != bench), None)


class ParallelCityPassive(Passive):
    """3-Bench on one side, -20 from Grass/Fire/Water attacks on the other."""

    def bench_capacity(self, player_id, carrier):
        return 3 if player_id == bench_side(carrier) else None

    def modify_damage_dealt(self, calc, carrier):
        if not calc.is_attack or calc.attacker is None:
            return
        if calc.attacker.owning_player_id != _damage_side(carrier):
            return
        types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        if any(t in _REDUCED_TYPES for t in types):
            calc.amount = max(0, calc.amount - 20)

card = StadiumCardDef(
    guid="77d73cc0-02bd-5f76-af1c-a81dfe223324",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.xy8.trainercards.parallelcity_xy8_145.name",
    display_name="Parallel City",
    searchable_by=["Parallel City", "Stadium", "ParallelCity"],
    subtypes=["Stadium"],
    collector_number=145,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=ParallelCityPassive(),
    orientation_choices=[
        (
            "Orientação normal",
            "Seu dano de Grama, Fogo e Água é reduzido; o Banco adversário fica limitado a 3.",
        ),
        (
            "Orientação invertida",
            "Seu Banco fica limitado a 3; o dano de Grama, Fogo e Água adversário é reduzido.",
        ),
    ],
    allows_same_name_replacement=True,
)
