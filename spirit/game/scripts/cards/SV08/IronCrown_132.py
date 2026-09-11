from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f60779bf-7f1e-52b4-9ff5-f2394bd6c1ba",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronCrown.Name",
    display_name="Iron Crown",
    searchable_by=["Iron Crown", "Basic", "Future", "IronCrown"],
    subtypes=["Basic", "Future"],
    collector_number=132,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=1023,
    abilities=[
        Attack(
            title="Deleting Slash",
            game_text="If your opponent has 3 or more Benched Pokémon, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
