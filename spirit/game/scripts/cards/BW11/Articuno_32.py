from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage

card = PokemonCardDef(
    guid="bc9d2f34-7301-5f21-bf82-77e087a463ef",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno","Basic","Articuno"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
