from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8ed8207-bac7-5815-b635-3de0729a4a1f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    display_name='Tandemaus',
    searchable_by=['Tandemaus', 'Basic', 'Tandemaus'],
    subtypes=['Basic'],
    collector_number=160,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=924,
    abilities=[
        Attack(
            title='Double Hit',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
