from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2c5a5858-6077-53b0-9c04-1b7be4856ce6",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion","Basic","Virizion"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    abilities=[
        Ability(
            title="Justified",
            game_text="Each of this Pokémon's attacks does 50 more damage to Darkness Pokémon (before applying Weakness and Resistance).",
            passive=bw_legacy_passive("Each of this Pokémon's attacks does 50 more damage to Darkness Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
