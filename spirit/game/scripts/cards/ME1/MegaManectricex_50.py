from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="5262c48a-d8d0-52cf-a3d8-665211dc0b53",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaManectricex.Name",
    display_name="Mega Manectric ex",
    searchable_by=["Mega Manectric ex", "Stage 1", "MEGA", "ex", "SV_Mega", "MegaManectricex"],
    subtypes=["Stage 1", "MEGA", "ex", "SV_Mega"],
    collector_number=50,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Flash Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title="Riotous Blasting",
            game_text="You may discard all Energy from this Pokémon and have this attack do 130 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
