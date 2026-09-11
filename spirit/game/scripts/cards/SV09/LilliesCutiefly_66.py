from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2ebb12f9-3546-534d-bcbe-b0d7e30097ef",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    display_name="Lillie's Cutiefly",
    searchable_by=["Lillie's Cutiefly", "Basic", "LilliesCutiefly"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=742,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
