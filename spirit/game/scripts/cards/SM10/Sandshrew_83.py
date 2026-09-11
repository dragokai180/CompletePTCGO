from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c704189b-7f5d-5643-a503-3c8ab955eb23',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name',
    display_name='Sandshrew',
    searchable_by=['Sandshrew', 'Basic', 'Sandshrew'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=27,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
