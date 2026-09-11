from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6371dd55-a0be-5958-8525-ea3254ad694c',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name',
    display_name='Aegislash',
    searchable_by=['Aegislash', 'Stage 2', 'Aegislash'],
    subtypes=['Stage 2'],
    collector_number=109,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    family_id=679,
    abilities=[
        Ability(
            title='Royal Guard',
            game_text='This Pokémon takes 40 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 40 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Shield Bash',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
