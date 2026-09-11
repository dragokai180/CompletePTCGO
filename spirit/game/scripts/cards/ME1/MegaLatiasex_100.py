from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="78c2d964-4213-5da3-ba22-d53df9946242",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLatiasex.Name",
    display_name="Mega Latias ex",
    searchable_by=["Mega Latias ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaLatiasex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=100,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title="Illusory Impulse",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=300,
            effect=standard_attack,
        ),
    ],
)
