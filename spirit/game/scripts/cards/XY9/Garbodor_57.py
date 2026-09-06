"""Garbodor (XY - BREAKpoint 57/122).

Stage 1 Psychic Pokemon, evolves from Trubbish. HP 100, weakness Psychic x2,
no resistance, retreat 3.

  Garbotoxin (Ability)  If this Pokemon has a Pokemon Tool card attached to
                        it, each Pokemon in play, in each player's hand, and
                        in each player's discard pile has no Abilities
                        (except for Garbotoxin).
  Offensive Bomb [PCCC] 60  Your opponent's Active Pokemon is now Confused
                        and Poisoned.

Garbotoxin is two locks wearing one name.

The in-play half is Klefki's Mischievous Lock with a different filter:
blocks_abilities, evaluated on the unfiltered passive set so no other lock
can switch it off, and skipping any Pokemon that itself has Garbotoxin so
the "except for Garbotoxin" clause holds for a second copy as well as for
this one.

The hand/discard half had no precedent. Every other lock in the game reads
"Pokemon in play", which is why _out_of_zone_ability_entries deliberately
ignored ability locks -- Path to the Peak must not reach those zones. Rather
than weaken that, this adds a second hook, blocks_out_of_play_abilities,
that only a lock naming those zones answers. It gates the same seven cards
the engine offers from hand or discard (Pyukumuku, Beedrill, Gengar, Ho-Oh
V, Empoleon, Talonflame ex).

The switch is the Tool, so it is re-read on every query: attach a Float
Stone and the lock comes on, Tool Scrapper it away and every Ability in the
game turns back on at once.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack, has_tool
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import Passive


def _has_garbotoxin(card) -> bool:
    """"except for Garbotoxin": read as "except cards carrying it", which is
    the same set of cards -- Garbotoxin is the only Ability those printings
    have."""
    definition = def_for(card.archetype_id)
    return any(
        getattr(a, "title", "") == "Garbotoxin"
        for a in (getattr(definition, "abilities", None) or [])
    )


class _GarbotoxinPassive(Passive):
    """While a Tool is attached, Abilities are off in play, in hand and in
    the discard -- for both players."""

    def blocks_abilities(self, pokemon, carrier):
        if not has_tool(carrier):
            return False
        return not _has_garbotoxin(pokemon)

    def blocks_out_of_play_abilities(self, card, carrier):
        if not has_tool(carrier):
            return False
        # "each Pokemon ... has no Abilities" -- a Trainer sitting in the
        # discard is not named by the text.
        if not is_pokemon_card(card):
            return False
        return not _has_garbotoxin(card)


card = PokemonCardDef(
    guid="90a4463b-49ec-5bd0-93c4-7bd0a758bd9a",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Garbotoxin",
            game_text=(
                "If this Pokémon has a Pokémon Tool card attached to it, each "
                "Pokémon in play, in each player's hand, and in each player's "
                "discard pile has no Abilities (except for Garbotoxin)."
            ),
            passive=_GarbotoxinPassive(),
        ),
        Attack(
            title="Offensive Bomb",
            game_text=(
                "Your opponent's Active Pokémon is now Confused and Poisoned."
            ),
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=condition_attack(
                SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)
