from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c024e725-d68d-57c0-8a81-1a92231da5ee',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name',
    display_name='Solgaleo',
    searchable_by=['Solgaleo', 'Stage 2', 'Solgaleo'],
    subtypes=['Stage 2'],
    collector_number=99,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=791,
    abilities=[
        Ability(
            title='Full Metal Body',
            game_text='If this Pokémon has any Metal Energy attached to it, it has no Weakness.',
            passive=standard_passive('If this Pokémon has any Metal Energy attached to it, it has no Weakness.'),
        ),
        Attack(
            title='Rising Dash',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
