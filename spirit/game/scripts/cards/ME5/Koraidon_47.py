from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1e043122-0a24-51bb-8eb9-9d745ff64692",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Koraidon"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=1007,
    abilities=[
        Attack(
            title="Battle Claw",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Gaia Impact",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
