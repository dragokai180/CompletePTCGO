from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70565aac-edee-51da-83e4-9484ace6fc70',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    display_name='Pidgeotto',
    searchable_by=['Pidgeotto', 'Stage 1', 'Pidgeotto'],
    subtypes=['Stage 1'],
    collector_number=123,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name',
    family_id=16,
    abilities=[
        Ability(
            title='Air Mail',
            game_text='Once during your turn (before your attack), you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card on the bottom of your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Gust',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
