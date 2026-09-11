from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c4d98f5-8a0c-570d-bb56-ae453fae85f5',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    display_name='Caterpie',
    searchable_by=['Caterpie', 'Basic', 'Caterpie'],
    subtypes=['Basic'],
    collector_number=2,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=10,
    abilities=[
        Ability(
            title='Pupate',
            game_text='Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hook',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
