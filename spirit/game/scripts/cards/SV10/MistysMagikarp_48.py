from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="62fc1153-8eff-57de-ab01-055114159b38",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    display_name="Misty's Magikarp",
    searchable_by=["Misty's Magikarp", "Basic", "MistysMagikarp"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=129,
    abilities=[
        Ability(
            title="So Submerged",
            game_text="As long as this Pokémon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon.",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon."),
        ),
        Attack(
            title="Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
