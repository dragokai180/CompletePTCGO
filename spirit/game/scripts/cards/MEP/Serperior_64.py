from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="213de5ad-e329-5a5c-aca4-d9706515b2f6",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=64,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    abilities=[
        Attack(
            title="Regal Command",
            game_text="This attack does 20 damage for each of your Pokémon in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Solar Coiling",
            game_text="If Rosa's Encouragement is in your discard pile, this attack does 150 more damage.",
            cost={PokemonTypes.GRASS: 3},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
