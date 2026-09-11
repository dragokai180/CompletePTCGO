from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89573c2f-2180-5434-a022-a33d158a93c4',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name',
    display_name='Victini',
    searchable_by=['Victini', 'Basic', 'Victini'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=494,
    abilities=[
        Attack(
            title='V-Beatdown',
            game_text='This attack does 20 damage for each of your Basic Pokémon in play.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
