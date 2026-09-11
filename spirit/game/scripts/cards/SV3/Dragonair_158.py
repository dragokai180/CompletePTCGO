from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1985aec-a281-5e27-8a0b-f33250f3c2cd',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    display_name='Dragonair',
    searchable_by=['Dragonair', 'Stage 1', 'Dragonair'],
    subtypes=['Stage 1'],
    collector_number=158,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Dragon Tail',
            game_text='Flip 2 coins. This attack does 70 damage for each heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
