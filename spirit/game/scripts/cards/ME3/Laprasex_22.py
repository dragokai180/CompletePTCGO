from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="0ff8e615-0321-58d4-9b41-549f6960143c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Laprasex.Name",
    display_name="Lapras ex",
    searchable_by=["Lapras ex", "Basic", "ex", "Laprasex"],
    subtypes=["Basic", "ex"],
    collector_number=22,
    set_code="ME3",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title="Hydro Turn",
            game_text="This attack does 30 damage for each Water Energy attached to this Pokémon. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 3},
            damage=140,
        ),
    ],
)
