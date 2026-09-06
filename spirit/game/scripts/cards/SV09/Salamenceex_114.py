"""Salamence ex (SV - Journey Together 114/159).

Stage 2 Dragon Pokemon ex, evolves from Shelgon. HP 320, no weakness, no
resistance, retreat cost 2.

  Wide Blast    [RCC]      50 damage to each of your opponent's Benched
                           Pokemon. (Don't apply Weakness and Resistance for
                           Benched Pokemon.)
  Dragon Impact [RWCC] 300 Discard 2 Energy from this Pokemon.

Both are existing shapes used as-is. Wide Blast is spread_damage at its
defaults -- the opponent's side, Active excluded -- and the parenthetical is
the engine's own behaviour for bench damage rather than something the card
asks for. Dragon Impact is self_energy_discard_attack, which deals the
printed damage first and discards afterwards, matching the printed order.

The whole line is in the pool (Bagon and Shelgon, SWSH7, family 371), so
this can be evolved into normally as well as reached from the discard.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    self_energy_discard_attack, spread_damage,
)

card = PokemonCardDef(
    guid="6ad55bd5-4b16-5654-8291-b02865cd5d2a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=114,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Wide Blast",
            game_text=(
                "This attack does 50 damage to each of your opponent's "
                "Benched Pokémon. (Don't apply Weakness and Resistance for "
                "Benched Pokémon.)"
            ),
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=spread_damage(50),
        ),
        Attack(
            title="Dragon Impact",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={
                PokemonTypes.FIRE: 1,
                PokemonTypes.WATER: 1,
                PokemonTypes.COLORLESS: 2,
            },
            damage=300,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
