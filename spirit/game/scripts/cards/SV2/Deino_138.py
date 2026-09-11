from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a4b0486-84f5-5634-8ca3-4b1a58e4599d',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name',
    display_name='Deino',
    searchable_by=['Deino', 'Basic', 'Deino'],
    subtypes=['Basic'],
    collector_number=138,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=633,
    abilities=[
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
