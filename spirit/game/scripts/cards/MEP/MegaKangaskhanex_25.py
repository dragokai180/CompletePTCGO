from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ff775e20-33ce-5850-a2f5-13054b67a67e",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaKangaskhanex.Name",
    display_name="Mega Kangaskhan ex",
    searchable_by=["Mega Kangaskhan ex", "Basic", "MegaKangaskhanex"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    abilities=[
        Ability(
            title="Run Errand",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Draw 2 cards. You can't use more than 1 Run Errand Ability each turn.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Rapid-Fire Combo",
            game_text="Flip a coin until you get tails. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
