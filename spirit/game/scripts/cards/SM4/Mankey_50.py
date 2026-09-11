from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='45640307-ede2-5473-a932-4d5ab9f8a9d9',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    display_name='Mankey',
    searchable_by=['Mankey', 'Basic', 'Mankey'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=56,
    abilities=[
        Attack(
            title='Three-Step Strike',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
