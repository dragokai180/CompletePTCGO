from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="8b0b7d51-9926-5c28-8c65-020d6c27ac54",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFire.Name",
    display_name="Gouging Fire",
    searchable_by=["Gouging Fire", "Basic", "Ancient", "GougingFire"],
    subtypes=["Basic", "Ancient"],
    collector_number=38,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=1020,
    abilities=[
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Blazing Charge",
            game_text="If your opponent has 4 or fewer Prize cards remaining, this attack does 70 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
