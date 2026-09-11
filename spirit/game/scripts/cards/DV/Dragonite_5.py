from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.bw10 import destructive_beam

card = PokemonCardDef(
    guid="94502a0c-2793-5a19-98ee-549ed90f6bf5",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite","Stage 2","Dragonite"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=destructive_beam,
        ),
        Attack(
            title="Hurricane Tail",
            game_text="Flip 4 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=60),
        ),
    ],
)
