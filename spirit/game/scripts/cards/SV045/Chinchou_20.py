from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9387ec90-d625-5030-8c67-b021e934b0d8',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    display_name='Chinchou',
    searchable_by=['Chinchou', 'Basic', 'Chinchou'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=170,
    abilities=[
        Attack(
            title='Shine On',
            game_text='Look at the top card of your deck. You may put that card on the bottom of your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tiny Charge',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
