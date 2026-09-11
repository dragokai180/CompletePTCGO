from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="24fc1c63-e217-5aa0-8ac2-9585a1f3c751",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=245,
    abilities=[
        Attack(
            title="Crystal Fall",
            game_text="If you have at least 4 Water Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
