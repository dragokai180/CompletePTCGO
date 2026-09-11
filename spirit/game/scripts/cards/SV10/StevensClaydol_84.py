from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1ac58205-d4cd-5887-b0e5-e438cca0e17f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensClaydol.Name",
    display_name="Steven's Claydol",
    searchable_by=["Steven's Claydol", "Stage 1", "StevensClaydol"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBaltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Eerie Light",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Clay Blast",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
