from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f05c84ec-f942-5674-b101-ef8ba04830c1',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name',
    display_name='Swadloon',
    searchable_by=['Swadloon', 'Stage 1', 'Swadloon'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name',
    family_id=540,
    abilities=[
        Ability(
            title='Swaddling Leaves',
            game_text='This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
