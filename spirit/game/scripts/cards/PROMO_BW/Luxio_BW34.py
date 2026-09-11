from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.bw10 import creepy_wind, wind_blast

card = PokemonCardDef(
    guid="056e4eff-e4fa-51ab-a3d4-46e4fee2553d",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    display_name="Luxio",
    searchable_by=["Luxio","Stage 1","Luxio"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    abilities=[
        Attack(
            title="Dazzle Blast",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=creepy_wind,
        ),
        Attack(
            title="Random Spark",
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(40, pool="any"),
        ),
    ],
)
