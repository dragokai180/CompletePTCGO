from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="3e3572db-29dc-5e42-aa8e-1070deb0a68b",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeoex.Name",
    display_name="Keldeo ex",
    searchable_by=["Keldeo ex", "Basic", "ex", "Keldeoex"],
    subtypes=["Basic", "ex"],
    collector_number=30,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=647,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
