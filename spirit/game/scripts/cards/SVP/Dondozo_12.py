from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b573d352-feff-580a-a42c-a95b6df21bfc',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name',
    display_name='Dondozo',
    searchable_by=['Dondozo', 'Basic', 'Dondozo'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=977,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title='Dangerous Wave',
            game_text='Flip 2 coins. If both of them are heads, this attack does 100 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
