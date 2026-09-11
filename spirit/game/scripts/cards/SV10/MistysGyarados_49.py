from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d4a3a1f0-636c-5241-a80d-7a4cad0cc377",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGyarados.Name",
    display_name="Misty's Gyarados",
    searchable_by=["Misty's Gyarados", "Stage 1", "MistysGyarados"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Splashing Panic",
            game_text="Discard the top 7 cards of your deck, and this attack does 70 damage for each Misty's Pokémon that you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=70,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
