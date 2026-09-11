from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4ad51ba8-3d6e-5bbe-9e87-ce16af607e40",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Round",
            game_text="This attack does 70 damage for each of your Pokémon in play that has the Round attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)
