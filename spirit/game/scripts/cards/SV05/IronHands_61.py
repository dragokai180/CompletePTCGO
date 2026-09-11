from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="01634bf6-d718-53fd-bc2e-d34e50516937",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronHands.Name",
    display_name="Iron Hands",
    searchable_by=["Iron Hands", "Basic", "Future", "IronHands"],
    subtypes=["Basic", "Future"],
    collector_number=61,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=992,
    abilities=[
        Attack(
            title="Volt Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title="Superalloy Hands",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
