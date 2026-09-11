from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af06fa2f-377b-5824-ad8e-3c69853bc3f5',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name',
    display_name='Kingambit',
    searchable_by=['Kingambit', 'Stage 2', 'Kingambit'],
    subtypes=['Stage 2'],
    collector_number=134,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name',
    family_id=624,
    abilities=[
        Ability(
            title='Leadership',
            game_text="Your Basic Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("Your Basic Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Hack At',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
