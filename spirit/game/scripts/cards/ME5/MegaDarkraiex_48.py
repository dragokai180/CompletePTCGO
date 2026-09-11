from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="86dbf1e9-6e0c-59eb-a93d-736338fe9344",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDarkraiex.Name",
    display_name="Mega Darkrai ex",
    searchable_by=["Mega Darkrai ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaDarkraiex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=48,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=491,
    abilities=[
        Attack(
            title="Dusk Raid",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 110 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=110,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Abyss Eye",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, it is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 3},
            effect=standard_attack,
        ),
    ],
)
