from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f83f7a9a-6c52-5e7f-8bf0-d9808fd7dd3a',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name',
    display_name='Registeel',
    searchable_by=['Registeel', 'Basic', 'Registeel'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Attack(
            title='Iron Head',
            game_text='Flip a coin until you get tails. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Forbidden Iron Hammer',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, discard an Energy attached to that Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
