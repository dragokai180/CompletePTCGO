from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d3b9c10-111c-5d63-9d28-38c585d1cdae',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name',
    display_name='Trevenant',
    searchable_by=['Trevenant', 'Stage 1', 'Trevenant'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    family_id=708,
    abilities=[
        Attack(
            title='Poltergeist',
            game_text='Your opponent reveals their hand. This attack does 30 damage for each Trainer card you find there.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Horn Leech',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
