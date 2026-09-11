from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="8f9dc621-1300-54a7-99ff-def64cfa54ce",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmegaex.Name",
    display_name="Yanmega ex",
    searchable_by=["Yanmega ex", "Stage 1", "ex", "Yanmegaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=3,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Ability(
            title="Buzzing Boost",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may search your deck for up to 3 Basic Grass Energy cards and attach them to this Pokémon. Then, shuffle your deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Jet Cyclone",
            game_text="Move 3 Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=standard_attack,
        ),
    ],
)
