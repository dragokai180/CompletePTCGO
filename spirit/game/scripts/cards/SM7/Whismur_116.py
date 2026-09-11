from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1c358bc-9743-5e66-8c68-dfea6639d5e7',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name',
    display_name='Whismur',
    searchable_by=['Whismur', 'Basic', 'Whismur'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=293,
    abilities=[
        Attack(
            title='Bawl',
            game_text="You can use this attack only if you go second, and only on your first turn. Your opponent can't play any Trainer cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
