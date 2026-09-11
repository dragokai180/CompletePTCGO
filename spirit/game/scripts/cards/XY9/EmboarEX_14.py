from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3adff194-a0a5-5445-a67b-67a031d05544',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EmboarEX.Name',
    display_name='Emboar-EX',
    searchable_by=['Emboar-EX', 'Basic', 'EX', 'EmboarEX'],
    subtypes=['Basic', 'EX'],
    collector_number=14,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=500,
    abilities=[
        Attack(
            title='Spiral Punch',
            game_text='Flip a coin until you get tails. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Strong Flare',
            game_text='Discard 2 Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
