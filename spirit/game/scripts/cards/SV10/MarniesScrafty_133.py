from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b96493bd-d4d0-54ab-a5b8-749f7195ab12",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScrafty.Name",
    display_name="Marnie's Scrafty",
    searchable_by=["Marnie's Scrafty", "Stage 1", "MarniesScrafty"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
