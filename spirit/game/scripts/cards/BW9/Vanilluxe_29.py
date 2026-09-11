from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive

card = PokemonCardDef(
    guid="8ec29741-4d40-5971-b319-df414f489a47",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe","Stage 2","Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    abilities=[
        Attack(
            title="ChillMAX",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=60),
        ),
        Attack(
            title="Cold Breath",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=powder_snow,
        ),
    ],
)
