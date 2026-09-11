from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dbce57a4-2a18-50af-a238-e485f50d7107',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name',
    display_name='Maschiff',
    searchable_by=['Maschiff', 'Basic', 'Maschiff'],
    subtypes=['Basic'],
    collector_number=141,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=942,
    abilities=[
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
