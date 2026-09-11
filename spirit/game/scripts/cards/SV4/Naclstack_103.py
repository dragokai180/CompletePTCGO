from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='26930fc6-e2a1-5f59-84c6-57c153209ebd',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name',
    display_name='Naclstack',
    searchable_by=['Naclstack', 'Stage 1', 'Naclstack'],
    subtypes=['Stage 1'],
    collector_number=103,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name',
    family_id=932,
    abilities=[
        Attack(
            title='Rocky Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
