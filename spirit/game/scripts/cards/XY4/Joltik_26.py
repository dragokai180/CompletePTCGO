from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ddf7553f-dc08-5c4d-b582-fd4c0d32262e',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    display_name='Joltik',
    searchable_by=['Joltik', 'Basic', 'Joltik'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=595,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Night March',
            game_text='This attack does 20 damage times the number of Pokémon in your discard pile that have the Night March attack.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
