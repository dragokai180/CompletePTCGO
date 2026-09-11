from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b3e801d7-1236-5add-8b3c-615be358bf35",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name",
    display_name="Tyrantrum",
    searchable_by=["Tyrantrum", "Stage 2", "Tyrantrum"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    abilities=[
        Ability(
            title="Tyrannically Gutsy",
            game_text="If this Pokémon has any Special Energy attached, it gets +150 HP.",
            passive=standard_passive("If this Pokémon has any Special Energy attached, it gets +150 HP."),
        ),
        Attack(
            title="Wreak Havoc",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
