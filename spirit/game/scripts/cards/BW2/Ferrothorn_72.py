from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="e950224f-f818-599c-9674-b2f36f1ee14a",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn","Stage 1","Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    abilities=[
        Attack(
            title="Steel Feelers",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Gyro Ball",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. Then, your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=bw_legacy_attack,
        ),
    ],
)
