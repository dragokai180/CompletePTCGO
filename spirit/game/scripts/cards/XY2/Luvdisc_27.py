from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='81353754-84ab-5142-b7bd-ae0303a7842b',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name',
    display_name='Luvdisc',
    searchable_by=['Luvdisc', 'Basic', 'Luvdisc'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=370,
    abilities=[
        Attack(
            title='Heart Wink',
            game_text="Flip a coin. If heads, your opponent can't draw a card at the beginning of his or her next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spike Draw',
            game_text='Draw a card.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
