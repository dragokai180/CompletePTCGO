from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3ebda73-baf3-5983-b843-c53b5e5ca9dd',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name',
    display_name='Victini ◇',
    searchable_by=['Victini ◇', 'Basic', 'Prism Star', 'Victini'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=7,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=494,
    abilities=[
        Attack(
            title='Infinity',
            game_text='This attack does 20 damage for each basic Energy card in your discard pile. Then, shuffle those cards into your deck.',
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
