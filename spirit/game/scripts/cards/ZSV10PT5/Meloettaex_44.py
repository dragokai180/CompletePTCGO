from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2b37e5e9-c77a-5417-afa0-c69a44d6205a",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloettaex.Name",
    display_name="Meloetta ex",
    searchable_by=["Meloetta ex", "Basic", "ex", "Meloettaex"],
    subtypes=["Basic", "ex"],
    collector_number=44,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=648,
    abilities=[
        Ability(
            title="Debut Performance",
            game_text="If you go first, this Pokémon can use attacks during your first turn.",
            passive=standard_passive("If you go first, this Pokémon can use attacks during your first turn."),
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
