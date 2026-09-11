from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="35014ea7-a5f3-512b-af92-36725997915f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesLiepard.Name",
    display_name="Marnie's Liepard",
    searchable_by=["Marnie's Liepard", "Stage 1", "MarniesLiepard"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesPurrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Pointy Claws",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
