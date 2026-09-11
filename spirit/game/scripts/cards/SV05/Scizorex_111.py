from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="cb547988-9487-5efe-bbc5-a91613c06567",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizorex.Name",
    display_name="Scizor ex",
    searchable_by=["Scizor ex", "Stage 1", "ex", "Scizorex"],
    subtypes=["Stage 1", "ex"],
    collector_number=111,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title="Cross Breaker",
            game_text="Discard up to 2 Metal Energy from this Pokémon. This attack does 120 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
