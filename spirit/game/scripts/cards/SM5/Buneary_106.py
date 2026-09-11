from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='25e48237-e65b-58ab-8494-1a2a090d6853',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name',
    display_name='Buneary',
    searchable_by=['Buneary', 'Basic', 'Buneary'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=427,
    abilities=[
        Attack(
            title='Weak Kneed',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Skip',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
