from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c944b6a4-7fea-5a0a-a7ee-8fc3a6e792f2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozoex.Name",
    display_name="Dondozo ex",
    searchable_by=["Dondozo ex", "Basic", "ex", "Dondozoex"],
    subtypes=["Basic", "ex"],
    collector_number=66,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=977,
    abilities=[
        Attack(
            title="Avenging Billow",
            game_text="This attack does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Dynamic Dive",
            game_text="You may do 120 more damage. If you do, this Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
