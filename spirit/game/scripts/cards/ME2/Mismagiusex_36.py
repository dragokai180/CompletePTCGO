from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ff3166c0-bd6e-5559-a9a6-33e05c2bf5bf",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagiusex.Name",
    display_name="Mismagius ex",
    searchable_by=["Mismagius ex", "Stage 1", "ex", "Mismagiusex"],
    subtypes=["Stage 1", "ex"],
    collector_number=36,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Swirling Prose",
            game_text="As long as this Pokémon is in the Active Spot, whenever your opponent's Active Pokémon moves to the Bench during their turn, their new Active Pokémon is now Confused.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, whenever your opponent's Active Pokémon moves to the Bench during their turn, their new Active Pokémon is now Confused."),
        ),
        Attack(
            title="Hexa-Magic",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
