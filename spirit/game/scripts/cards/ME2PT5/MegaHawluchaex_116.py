from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="92b4f074-ad88-532f-8942-be1e4447eded",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHawluchaex.Name",
    display_name="Mega Hawlucha ex",
    searchable_by=["Mega Hawlucha ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaHawluchaex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=116,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=701,
    abilities=[
        Ability(
            title="Tenacious Body",
            game_text="If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.",
            passive=standard_passive("If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10."),
        ),
        Attack(
            title="Somersault Dive",
            game_text="If a Stadium is in play, this attack does 140 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
