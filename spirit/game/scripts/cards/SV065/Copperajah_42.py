from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="e6591cec-883d-5d7f-8dcf-9aadcaf4b3ed",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1", "Copperajah"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Ability(
            title="Massive Body",
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand."),
        ),
        Attack(
            title="Nasal Lariat",
            game_text="You may do 100 more damage. If you do, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
