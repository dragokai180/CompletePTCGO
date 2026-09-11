from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1fa46cfc-6184-5201-bff2-13648bf187d6",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    abilities=[
        Attack(
            title="Retaliatory Claw",
            game_text="If this Pokémon's remaining HP is 50 or less, this attack does 170 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Cut",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
    ],
)
