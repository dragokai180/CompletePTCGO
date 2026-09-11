from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ca79a578-7a16-5a69-a96c-131054d0e7d7",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigoex.Name",
    display_name="Flamigo ex",
    searchable_by=["Flamigo ex", "Basic", "ex", "Flamigoex"],
    subtypes=["Basic", "ex"],
    collector_number=160,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title="Precise Beak",
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
