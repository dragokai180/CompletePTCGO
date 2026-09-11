from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="61b9d063-e7a9-5354-8913-322b7c57891a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscarada.Name",
    display_name="Meowscarada",
    searchable_by=["Meowscarada", "Stage 2", "Meowscarada"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Ability(
            title="Showtime",
            game_text="Once during your turn, if this Pokémon is on your Bench, you may switch it with your Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Rising Bloom",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
