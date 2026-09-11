from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="97a7a6ab-642f-5579-bcf3-2e4d3ab91358",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon2.Name",
    display_name="Team Rocket's Porygon2",
    searchable_by=["Team Rocket's Porygon2", "Stage 1", "TeamRocketsPorygon2"],
    subtypes=["Stage 1"],
    collector_number=154,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon.Name",
    family_id=137,
    abilities=[
        Attack(
            title="R Command",
            game_text="This attack does 20 damage for each Supporter card that has \"Team Rocket\" in its name in your discard pile.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
