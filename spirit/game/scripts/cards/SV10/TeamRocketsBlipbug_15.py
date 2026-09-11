from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1bfea679-63e7-54eb-af64-b8b449e799b0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsBlipbug.Name",
    display_name="Team Rocket's Blipbug",
    searchable_by=["Team Rocket's Blipbug", "Basic", "TeamRocketsBlipbug"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=824,
    abilities=[
        Attack(
            title="Searching Eyes",
            game_text="Look at 1 of your opponent's face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
