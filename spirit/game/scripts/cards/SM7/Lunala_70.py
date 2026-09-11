from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='50280326-6540-5fd4-9c09-e71bd2617609',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name',
    display_name='Lunala',
    searchable_by=['Lunala', 'Stage 2', 'Lunala'],
    subtypes=['Stage 2'],
    collector_number=70,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=792,
    abilities=[
        Ability(
            title='Shadow Shield',
            game_text='If this Pokémon has any Psychic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('If this Pokémon has any Psychic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Full Moon Ray',
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
