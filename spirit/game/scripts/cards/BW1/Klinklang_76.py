from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers, movable_energy_condition

card = PokemonCardDef(
    guid="c4b694a1-3bba-5ee5-a1e0-80d5582db182",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang","Stage 2","Klinklang"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    abilities=[
        Ability(
            title="Shift Gear",
            game_text="As often as you like during your turn (before your attack), you may move a Metal Energy attached to 1 of your Pokémon to another of your Pokémon.",
            activation="unlimited",
            effect=bw_legacy_ability,
            condition=movable_energy_condition(PokemonTypes.METAL),
        ),
        Attack(
            title="Gear Grind",
            game_text="Flip 2 coins. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=80),
        ),
    ],
)
