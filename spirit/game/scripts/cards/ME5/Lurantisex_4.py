from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="fa94e14b-1206-58c4-a523-d0405cac2418",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantisex.Name",
    display_name="Lurantis ex",
    searchable_by=["Lurantis ex", "Stage 1", "ex", "Lurantisex"],
    subtypes=["Stage 1", "ex"],
    collector_number=4,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Attack(
            title="Lively Cutter",
            game_text="If this Pokémon was healed during this turn, this attack does 200 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
