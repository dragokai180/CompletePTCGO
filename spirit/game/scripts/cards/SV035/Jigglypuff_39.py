from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f3a44a5-4b4b-5843-92f8-5d50b61a895f',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    display_name='Jigglypuff',
    searchable_by=['Jigglypuff', 'Basic', 'Jigglypuff'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=39,
    abilities=[
        Attack(
            title='Lead',
            game_text='Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stompy Stomp',
            game_text='Flip 2 coins. This attack does 20 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
