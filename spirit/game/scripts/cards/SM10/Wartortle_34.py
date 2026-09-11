from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b6753f27-c35f-533e-be65-bcc14ab2a51a',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name',
    display_name='Wartortle',
    searchable_by=['Wartortle', 'Stage 1', 'Wartortle'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name',
    family_id=7,
    abilities=[
        Ability(
            title='Solid Shell',
            game_text='This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Aqua Slash',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
