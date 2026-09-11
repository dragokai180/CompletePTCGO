from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2fb04ba1-b2c6-59b2-8e93-32846118619c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=483,
    abilities=[
        Attack(
            title="Time Manipulation",
            game_text="Search your deck for 2 cards, shuffle your deck, then put those cards on top of it in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Buster Tail",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
