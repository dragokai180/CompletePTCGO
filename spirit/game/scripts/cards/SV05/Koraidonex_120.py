"""Koraidon ex (SV - Temporal Forces 120/162).

Basic Dragon Pokemon ex, Ancient. HP 230, no weakness, no resistance,
retreat cost 2.

  Retribution Strike [CC]  20+  This attack does 10 more damage for each
                                damage counter on this Pokemon.
  Kaiser Tackle      [RFF] 280  This Pokemon also does 60 damage to itself.

Both shapes already exist: damage_per with a base (Sudowoodo's Flail counts
the same counters, just without the flat 20 under it) and recoil_attack,
which deals the printed damage and then hits the attacker with no weakness
or resistance applied.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_counters_on, damage_per, recoil_attack,
)

card = PokemonCardDef(
    guid="9269ea9f-2555-5ea7-ac12-562bf02974d8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex", "Ancient", "Koraidonex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=120,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=1007,
    abilities=[
        Attack(
            title="Retribution Strike",
            game_text=(
                "This attack does 10 more damage for each damage counter "
                "on this Pokémon."
            ),
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=20),
        ),
        Attack(
            title="Kaiser Tackle",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={
                PokemonTypes.FIRE: 1,
                PokemonTypes.FIGHTING: 2,
            },
            damage=280,
            effect=recoil_attack(60),
        ),
    ],
)
