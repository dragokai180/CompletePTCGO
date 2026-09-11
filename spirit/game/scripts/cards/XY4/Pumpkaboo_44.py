from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b4690fd-9d04-5d5e-84ba-df70f63533c3',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    display_name='Pumpkaboo',
    searchable_by=['Pumpkaboo', 'Basic', 'Pumpkaboo'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=710,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Night March',
            game_text='This attack does 20 damage times the number of Pokémon in your discard pile that have the Night March attack.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
