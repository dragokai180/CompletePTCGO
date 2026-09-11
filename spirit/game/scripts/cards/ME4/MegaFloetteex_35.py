from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="08785f2e-6939-5a9e-abc0-b2c28d3d1bb8",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFloetteex.Name",
    display_name="Mega Floette ex",
    searchable_by=["Mega Floette ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaFloetteex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=35,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=670,
    abilities=[
        Attack(
            title="Gentle Light",
            game_text="Heal 30 damage from each Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Eternity Bloom",
            game_text="Search your deck for up to 4 Basic Psychic Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
