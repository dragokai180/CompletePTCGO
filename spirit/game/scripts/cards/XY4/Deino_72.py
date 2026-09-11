from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4c25feb-cdfc-538c-99ac-31680418bcb4',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name',
    display_name='Deino',
    searchable_by=['Deino', 'Basic', 'Deino'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=633,
    abilities=[
        Attack(
            title='Gnaw Off',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
