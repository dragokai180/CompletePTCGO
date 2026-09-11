from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='484f1bab-aaaa-58a7-82cb-aa61e1d42ec4',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name',
    display_name='Quilladin',
    searchable_by=['Quilladin', 'Stage 1', 'Quilladin'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name',
    family_id=650,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Pin Missile',
            game_text='Flip 4 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
