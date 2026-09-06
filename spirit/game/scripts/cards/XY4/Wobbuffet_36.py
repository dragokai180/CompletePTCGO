"""Wobbuffet (XY - Phantom Forces 36/119).

Basic Psychic Pokemon. HP 110, weakness Psychic x2, no resistance, retreat 2.

  Bide Barricade (Ability)  If this Pokemon is your Active Pokemon, each
                        Pokemon in play, in each player's hand, and in each
                        player's discard pile has no Abilities (except for
                        Psychic Pokemon).
  Psychic Assault  [PC] 10+  10 more damage for each damage counter on your
                        opponent's Active Pokemon.

The third card on Garbotoxin's pair of hooks, and the one that combines
every piece already here: Klefki's is_in_active_spot gate, Silent Lab's
"reaches hands and discard piles" via blocks_out_of_play_abilities, and an
exception clause keyed on type rather than on an Ability name.

Being Psychic itself, Wobbuffet is spared by its own exception, so unlike
Klefki and Garbodor this needs no separate carrier check -- the printed
"(except for Psychic Pokemon)" already covers it.

Note the scope: every Pokemon, not just Basics. A Stage 2 with an Ability
goes quiet too while this is Active.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_pokemon_card, is_pokemon_of_type
from spirit.game.session.passives import Passive


def _spared(card) -> bool:
    """"except for Psychic Pokemon"."""
    return is_pokemon_of_type(card, PokemonTypes.PSYCHIC)


class _BideBarricadePassive(Passive):
    """While Wobbuffet is Active, non-Psychic Pokemon have no Abilities --
    in play, in hand and in the discard pile, on both sides."""

    def blocks_abilities(self, pokemon, carrier):
        return is_in_active_spot(carrier) and not _spared(pokemon)

    def blocks_out_of_play_abilities(self, card, carrier):
        if not is_in_active_spot(carrier) or not is_pokemon_card(card):
            return False
        return not _spared(card)


card = PokemonCardDef(
    guid="aae17f34-9cf4-55bf-8b6a-8581e35d8c1a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Bide Barricade",
            game_text=(
                "If this Pokémon is your Active Pokémon, each Pokémon in "
                "play, in each player's hand, and in each player's discard "
                "pile has no Abilities (except for Psychic Pokémon)."
            ),
            passive=_BideBarricadePassive(),
        ),
        Attack(
            title="Psychic Assault",
            game_text=(
                "This attack does 10 more damage for each damage counter on "
                "your opponent's Active Pokémon."
            ),
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=damage_per(damage_counters_on("defender"), 10, base=10),
        ),
    ],
)
