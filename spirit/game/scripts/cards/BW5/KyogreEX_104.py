from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.bw10 import dimension_heal, strafe

card = PokemonCardDef(
    guid="2521b447-e193-5aa1-8ee8-818f45309a66",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name",
    display_name="Kyogre-EX",
    searchable_by=["Kyogre-EX","Basic","EX","KyogreEX"],
    subtypes=["Basic","EX"],
    collector_number=104,
    set_code="BW5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=strafe,
        ),
        Attack(
            title="Dual Splash",
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(50, pool="any", count=2, side="opponent"),
        ),
    ],
)
