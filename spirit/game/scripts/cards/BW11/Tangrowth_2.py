from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter

card = PokemonCardDef(
    guid="d84fe5b2-1824-5c09-90ea-223968795c1f",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth","Stage 1","Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    abilities=[
        Attack(
            title="Bind Down",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=dark_clamp,
        ),
        Attack(
            title="Flog",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
