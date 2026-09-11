from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='453985cd-24ac-52b8-b409-4741b3ae535b',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name',
    display_name='Corphish',
    searchable_by=['Corphish', 'Basic', 'Corphish'],
    subtypes=['Basic'],
    collector_number=42,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=341,
    abilities=[
        Attack(
            title='Vice Grip',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Knock Off',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
