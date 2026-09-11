from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import freestyle_strike, shoulder_throw
from spirit.game.card_effects.support_common import heal_targets

card = PokemonCardDef(
    guid="65f8fe29-927a-57db-91b5-0e962e4f3333",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair","Stage 1","Dragonair"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    abilities=[
        Attack(
            title="Healing Melody",
            game_text="Heal 10 damage from each of your Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=heal_targets(10, "each_own"),
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=freestyle_strike,
        ),
    ],
)
