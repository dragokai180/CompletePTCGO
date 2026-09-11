from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='627a21a5-7595-5e27-b90f-c0db14199344',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name',
    display_name='Skwovet',
    searchable_by=['Skwovet', 'Basic', 'Skwovet'],
    subtypes=['Basic'],
    collector_number=151,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=819,
    abilities=[
        Ability(
            title='Nest Stash',
            game_text='Once during your turn, you may shuffle your hand and put it on the bottom of your deck. If you put any cards on the bottom of your deck in this way, draw a card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
