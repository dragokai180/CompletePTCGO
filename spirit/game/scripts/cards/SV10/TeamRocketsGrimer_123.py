from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="9683c23d-755e-5dfe-8397-557ec40a478b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGrimer.Name",
    display_name="Team Rocket's Grimer",
    searchable_by=["Team Rocket's Grimer", "Basic", "TeamRocketsGrimer"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title="Corrosive Sludge",
            game_text="At the end of your opponent's next turn, discard the Defending Pokémon and all attached cards.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
