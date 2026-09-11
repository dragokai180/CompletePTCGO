from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='833bb9c0-be84-5e4c-a57d-de3fc04a24dc',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    display_name='Chansey',
    searchable_by=['Chansey', 'Basic', 'Chansey'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=113,
    abilities=[
        Attack(
            title='Nap',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lucky Punch',
            game_text="If you don't have exactly 7 cards in your hand, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
