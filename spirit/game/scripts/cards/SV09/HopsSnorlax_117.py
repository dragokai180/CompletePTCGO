from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="43304079-4772-5728-977c-8b1d78dd81c9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSnorlax.Name",
    display_name="Hop's Snorlax",
    searchable_by=["Hop's Snorlax", "Basic", "HopsSnorlax"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Ability(
            title="Extra Helpings",
            game_text="Attacks used by your Hop's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). The effect of Extra Helpings doesn't stack.",
            passive=standard_passive("Attacks used by your Hop's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). The effect of Extra Helpings doesn't stack."),
        ),
        Attack(
            title="Dynamic Press",
            game_text="This Pokémon also does 80 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
