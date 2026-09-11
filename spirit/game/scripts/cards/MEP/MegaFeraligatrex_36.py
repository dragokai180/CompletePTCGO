from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="5d0dea14-58d2-5b58-a7a8-986a94703e71",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFeraligatrex.Name",
    display_name="Mega Feraligatr ex",
    searchable_by=["Mega Feraligatr ex", "Stage 2", "MegaFeraligatrex"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=370,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    abilities=[
        Attack(
            title="Mortal Crunch",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
