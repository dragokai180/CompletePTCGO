from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e63eac22-97e8-5a6c-8723-8e163a515a9c',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    display_name='Ponyta',
    searchable_by=['Ponyta', 'Basic', 'Ponyta'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=77,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Stomp',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIRE: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
