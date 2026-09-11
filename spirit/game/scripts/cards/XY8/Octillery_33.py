from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    abyssal_hand, abyssal_hand_condition,
)


card = PokemonCardDef(
    guid='2aae843e-e0e7-50c3-b3be-a20f008dac41',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name',
    display_name='Octillery',
    searchable_by=['Octillery', 'Stage 1', 'Octillery'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    family_id=223,
    abilities=[
        Ability(
            title='Abyssal Hand',
            game_text='Once during your turn (before your attack), you may draw cards until you have 5 cards in your hand.',
            effect=abyssal_hand,
            condition=abyssal_hand_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hug',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
