from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="182d1fa8-7cb5-53a1-91a8-76ad5c9948c8",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalantex.Name",
    display_name="Bouffalant ex",
    searchable_by=["Bouffalant ex", "Basic", "ex", "Bouffalantex"],
    subtypes=["Basic", "ex"],
    collector_number=77,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=626,
    abilities=[
        Ability(
            title="Bouffer",
            game_text="This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title="Gold Breaker",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
