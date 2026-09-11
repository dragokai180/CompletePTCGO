from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d0d5789-1065-506c-88d3-5d75f7301ed6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name',
    display_name='Naclstack',
    searchable_by=['Naclstack', 'Stage 1', 'Naclstack'],
    subtypes=['Stage 1'],
    collector_number=122,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
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
            title='Salt Cannon',
            game_text='Flip 3 coins. This attack does 60 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
