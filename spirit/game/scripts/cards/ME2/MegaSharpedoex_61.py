from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2cbaba24-6777-56c6-b9c6-6c426fe77292",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSharpedoex.Name",
    display_name="Mega Sharpedo ex",
    searchable_by=["Mega Sharpedo ex", "Stage 1", "MEGA", "ex", "SV_Mega", "MegaSharpedoex"],
    subtypes=["Stage 1", "MEGA", "ex", "SV_Mega"],
    collector_number=61,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Greedy Fang",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title="Hungry Jaws",
            game_text="If this Pokémon has any damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
