from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='48e56f8f-68e5-51b2-9365-f15199d6e131',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name',
    display_name='Unown',
    searchable_by=['Unown', 'Basic', 'Unown'],
    subtypes=['Basic'],
    collector_number=91,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=201,
    abilities=[
        Ability(
            title='HAND',
            game_text='Once during your turn (before your attack), if this Pokémon is your Active Pokémon, and if you have 35 or more cards in your hand, you may use this Ability. If you do, you win this game.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hidden Power',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
