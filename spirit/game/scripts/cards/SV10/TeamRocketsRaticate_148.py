from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="97d56ebf-ff36-577e-91cb-eb6552ba0d7a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsRaticate.Name",
    display_name="Team Rocket's Raticate",
    searchable_by=["Team Rocket's Raticate", "Stage 1", "TeamRocketsRaticate"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Reckless Abandon",
            game_text="Flip 2 coins. If both of them are tails, this Pokémon also does 90 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
