from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='093b99c3-a8df-511f-acc4-a9d88a7889b8',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name',
    display_name='Whismur',
    searchable_by=['Whismur', 'Basic', 'Whismur'],
    subtypes=['Basic'],
    collector_number=117,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=293,
    abilities=[
        Attack(
            title='Wail',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
