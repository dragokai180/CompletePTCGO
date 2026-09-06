"""Sudowoodo (SM - Guardians Rising 66/145).

  Roadblock  "Your opponent can't have more than 4 Benched Pokemon. If
              they have 5 or more Benched Pokemon, they discard Benched
              Pokemon until they have 4 Pokemon on the Bench. If more
              than one effect changes the number of Benched Pokemon
              allowed, use the smaller number."

The mirror of Eternatus VMAX's Eternal Zone: a Pokemon Ability whose
passive answers bench_capacity, but for the OPPONENT's side and downward.

The tie-break the card spells out is already how the engine resolves it --
effective_bench_capacity takes max(1, min(overrides)) -- so Sudowoodo's 4
wins over Sky Field's 8 with no special casing on either card. The forced
discard down to 4 is enforce_bench_capacity(), the same shared helper that
handles Collapsed Stadium: a discard, not a Knock Out, so no prizes and no
ON_KNOCKED_OUT.

The art placed at spirit/assets/cards/SM2/Sudowoodo_66.png is the SM8b
(GX Ultra Shiny 054/150) Japanese print of the same card -- Guardians
Rising is the printing sets.json knows, and set_code is what AutoBundle
matches on (see the note in SM5/DialgaGX_100.py).
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class RoadblockPassive(Passive):
    """The opponent's Bench is capped at 4 while this Pokemon is in play."""

    def bench_capacity(self, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return None
        return 4


card = PokemonCardDef(
    guid="6a62e4e1-6bea-5a0d-8f5f-b53ede491e6c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Ability(
            title="Roadblock",
            game_text=(
                "Your opponent can't have more than 4 Benched Pokémon. "
                "If they have 5 or more Benched Pokémon, they discard "
                "Benched Pokémon until they have 4 Pokémon on the "
                "Bench. If more than one effect changes the number of "
                "Benched Pokémon allowed, use the smaller number."
            ),
            passive=RoadblockPassive(),
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
