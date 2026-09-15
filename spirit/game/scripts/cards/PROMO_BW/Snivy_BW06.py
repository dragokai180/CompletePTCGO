from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage

card = PokemonCardDef(
    guid="03c10da1-4cd9-5272-9caf-55d3b02467ca",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    display_name="Snivy",
    searchable_by=["Snivy","Basic","Snivy"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
