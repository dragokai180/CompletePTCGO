from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="95d86f13-7e04-5aa8-b7d6-eb27e73ce8b4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstoneex.Name",
    display_name="Houndstone ex",
    searchable_by=["Houndstone ex", "Stage 1", "ex", "Houndstoneex"],
    subtypes=["Stage 1", "ex"],
    collector_number=162,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Horrifying Fang",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
