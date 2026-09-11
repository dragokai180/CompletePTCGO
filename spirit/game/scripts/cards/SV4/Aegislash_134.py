from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6deb9f03-cba6-55ff-a2a8-fe09da8afb85',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name',
    display_name='Aegislash',
    searchable_by=['Aegislash', 'Stage 2', 'Aegislash'],
    subtypes=['Stage 2'],
    collector_number=134,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    family_id=679,
    abilities=[
        Ability(
            title='Mysterious Shield',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex and Pokémon V.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex and Pokémon V."),
        ),
        Attack(
            title='Hard Bashing',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
