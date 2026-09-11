from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16993456-111a-54c8-b738-13f5d405bda0',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    display_name='Mareanie',
    searchable_by=['Mareanie', 'Basic', 'Mareanie'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=747,
    abilities=[
        Attack(
            title='Spike Cannon',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
