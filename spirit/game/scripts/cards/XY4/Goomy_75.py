from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3495ddd5-e1d8-5766-ab02-e3db978083ae',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name',
    display_name='Goomy',
    searchable_by=['Goomy', 'Basic', 'Goomy'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=704,
    abilities=[
        Attack(
            title='Gooey',
            game_text='Heal 10 damage from this Pokémon',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1},
            damage=20,
        ),
    ],
)
