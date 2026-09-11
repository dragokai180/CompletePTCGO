from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e2fd951-55b2-5a97-a21c-c24091006e2a',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    display_name='Drilbur',
    searchable_by=['Drilbur', 'Basic', 'Drilbur'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=529,
    abilities=[
        Attack(
            title='Rising Lunge',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
