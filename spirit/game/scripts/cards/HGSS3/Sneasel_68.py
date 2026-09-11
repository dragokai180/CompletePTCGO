from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4da094a-5032-516b-9901-fd7fdf599386',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name',
    display_name='Sneasel',
    searchable_by=['Sneasel', 'Basic', 'Sneasel'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=215,
    abilities=[
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Beat Up',
            game_text='Flip a coin for each of your Pokémon in play. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
