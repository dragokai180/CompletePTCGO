from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b886a2f3-d519-5740-b223-1dc305d97e89',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    display_name='Drilbur',
    searchable_by=['Drilbur', 'Basic', 'Drilbur'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=529,
    abilities=[
        Attack(
            title='Rototiller',
            game_text='Shuffle a card from your discard pile into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
