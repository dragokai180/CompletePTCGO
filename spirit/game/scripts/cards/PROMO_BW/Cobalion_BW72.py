from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="4f80276f-90fc-5ce7-a0bd-afeac357f198",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion","Basic","Cobalion"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Justified",
            game_text="Each of this Pokémon's attack does 50 more damage to Darkness Pokémon (before applying Weakness and Resistance).",
            passive=bw_legacy_passive("Each of this Pokémon's attack does 50 more damage to Darkness Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)
