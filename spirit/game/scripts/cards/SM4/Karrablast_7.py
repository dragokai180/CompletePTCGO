from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f73fad69-6778-54dd-9ab2-42aaa900f5c7',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name',
    display_name='Karrablast',
    searchable_by=['Karrablast', 'Basic', 'Karrablast'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=588,
    abilities=[
        Ability(
            title='Shell On',
            game_text='Once during your turn (before your attack), you may discard a Shelmet from your hand. If you do, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
