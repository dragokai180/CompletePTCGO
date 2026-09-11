from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c16f9eff-fcaa-5eda-a1ee-4a5f245e0b1f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDragalgeex.Name",
    display_name="Mega Dragalge ex",
    searchable_by=["Mega Dragalge ex", "Stage 1", "MEGA", "ex", "SV_Mega", "MegaDragalgeex"],
    subtypes=["Stage 1", "MEGA", "ex", "SV_Mega"],
    collector_number=65,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Attack(
            title="Corrosive Liquid",
            game_text="Discard all Pokémon Tools and Special Energy from all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title="Pernicious Poison",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, place 16 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
)
