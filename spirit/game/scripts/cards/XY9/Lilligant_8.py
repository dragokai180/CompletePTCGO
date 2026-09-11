from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79bd7159-0356-59a5-9064-3d391457b7c4',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name',
    display_name='Lilligant',
    searchable_by=['Lilligant', 'Stage 1', 'Lilligant'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name',
    family_id=548,
    abilities=[
        Attack(
            title='Boo-Hoo',
            game_text='If your opponent attaches an Energy card from his or her hand to the Defending Pokémon during his or her next turn, that Pokémon will be Asleep.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Slice',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
