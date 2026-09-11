from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6291e40c-576a-5ba5-9f4e-6b6c32cac853",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=703,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pokémon is in play, it is Fighting and Psychic type.",
            passive=standard_passive("As long as this Pokémon is in play, it is Fighting and Psychic type."),
        ),
        Attack(
            title="Counter Jewel",
            game_text="If your opponent has 2 or fewer Prize cards remaining, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
