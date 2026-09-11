from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="9fea7406-c8f8-5955-b1d8-b2ac5606c567",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZygardeex.Name",
    display_name="Mega Zygarde ex",
    searchable_by=["Mega Zygarde ex", "Basic", "MegaZygardeex"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    abilities=[
        Attack(
            title="Gaia Wave",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance) .",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=standard_attack,
        ),
        Attack(
            title="Nullifying Zero",
            game_text="For each of your opponent's Pokémon, flip a coin. If heads, this attack does 150 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 5},
            effect=standard_attack,
        ),
    ],
)
