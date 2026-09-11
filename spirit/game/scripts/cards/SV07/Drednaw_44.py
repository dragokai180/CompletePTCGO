from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="2cbcc09f-886e-5a80-a406-36235caddcc9",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drednaw.Name",
    display_name="Drednaw",
    searchable_by=["Drednaw", "Stage 1", "Drednaw"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    family_id=833,
    abilities=[
        Ability(
            title="Impervious Shell",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon if that damage is 200 or more.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon if that damage is 200 or more."),
        ),
        Attack(
            title="Hard Crunch",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
