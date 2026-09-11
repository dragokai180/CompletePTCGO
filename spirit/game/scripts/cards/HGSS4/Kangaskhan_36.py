from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7802a94b-01e4-5da2-891c-49397e502754',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name',
    display_name='Kangaskhan',
    searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Split Spiral Punch',
            game_text='The Defending Pokémon is now Confused.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Dizzy Punch',
            game_text='Flip 2 coins. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
