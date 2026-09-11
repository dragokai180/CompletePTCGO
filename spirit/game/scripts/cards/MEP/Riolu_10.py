from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f2f02ae4-e34b-5324-8ceb-d7ae22076f4b",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu", "Basic", "Riolu"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    abilities=[
        Attack(
            title="Accelerating Stab",
            game_text="During your next turn, this Pokémon can't use Accelerating Stab.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
