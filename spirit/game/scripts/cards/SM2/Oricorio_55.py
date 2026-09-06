"""Oricorio (SM - Guardians Rising 55/145).

Basic Psychic Pokemon. HP 90, weakness Psychic x2, no resistance, retreat 1.

  Vital Dance (Ability)  When you play this Pokemon from your hand onto your
                        Bench during your turn, you may search your deck for
                        up to 2 basic Energy cards, reveal them, and put them
                        into your hand. Then, shuffle your deck.
  Casual Slap    [PC] 30

Wonder Tag with a different filter and count, which is now literally true:
Tapu Lele-GX's Wonder Tag, Lumineon V's Luminous Sign and this all print the
same sentence, so they share search_to_hand_on_play and differ only in the
predicate, the count and the two prompt strings.

No shared_once_per_turn, same as Tapu Lele-GX: the text carries no "you
can't use more than 1 ... each turn" clause, so two of these benched in one
turn each get their search.

The Japanese print is the SM1+ promo (023/051); the English printing with
this text is Guardians Rising 55.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import vital_dance

card = PokemonCardDef(
    guid="8b430d23-c36f-5037-bc0a-4b67f4a5ee40",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=741,
    abilities=[
        Ability(
            title="Vital Dance",
            game_text=(
                "When you play this Pokémon from your hand onto your Bench "
                "during your turn, you may search your deck for up to 2 basic "
                "Energy cards, reveal them, and put them into your hand. "
                "Then, shuffle your deck."
            ),
            trigger=Triggers.ON_PLAY,
            effect=vital_dance,
        ),
        Attack(
            title="Casual Slap",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
