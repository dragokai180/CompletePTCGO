from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="8e5a3f3d-ea18-53f8-8edb-339cf01a8c45",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glastrier.Name",
    display_name="Glastrier",
    searchable_by=["Glastrier", "Basic", "Glastrier"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=896,
    abilities=[
        Attack(
            title="Ice Shot",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="During your next turn, this Pokémon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 3},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
