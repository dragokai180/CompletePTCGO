from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2fd912b0-c95d-5ada-9309-48cdec30695b',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    display_name='Pawniard',
    searchable_by=['Pawniard', 'Basic', 'Pawniard'],
    subtypes=['Basic'],
    collector_number=148,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=624,
    abilities=[
        Attack(
            title='Triple Cutter',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
