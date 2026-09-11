from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8dd043c7-2636-55cf-a36f-40315f5a238f',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name',
    display_name='Alomomola',
    searchable_by=['Alomomola', 'Basic', 'Alomomola'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=594,
    abilities=[
        Attack(
            title='Super Deep Dive',
            game_text='Heal 30 damage from this Pokémon. Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
