from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4a4ea754-bbc8-5c24-aadb-c5169d97c583",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name",
    display_name="Castform Sunny Form",
    searchable_by=["Castform Sunny Form", "Basic", "CastformSunnyForm"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=351,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Sunny Assist",
            game_text="Move all Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
