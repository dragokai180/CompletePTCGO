from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2a80cbfb-b688-59bb-a0ce-20ef447c97de",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMuk.Name",
    display_name="Team Rocket's Muk",
    searchable_by=["Team Rocket's Muk", "Stage 1", "TeamRocketsMuk"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGrimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Gooped Up",
            game_text="Your opponent's Active Pokémon is now Confused. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title="Hazardous Venom",
            game_text="This attack does 100 damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
