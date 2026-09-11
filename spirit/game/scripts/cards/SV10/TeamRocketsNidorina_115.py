from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b77f5e3e-20b9-5187-86ba-ccaca7125a9e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorina.Name",
    display_name="Team Rocket's Nidorina",
    searchable_by=["Team Rocket's Nidorina", "Stage 1", "TeamRocketsNidorina"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoran.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Dark Awakening",
            game_text="Choose up to 2 of your Darkness Pokémon. For each of those Pokémon, search your deck for a card that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
        ),
    ],
)
