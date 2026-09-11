from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c11f11d5-e3dc-50bd-ab7d-35e265f9feb6',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name',
    display_name='Vibrava',
    searchable_by=['Vibrava', 'Stage 1', 'Vibrava'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name',
    family_id=328,
    abilities=[
        Attack(
            title='Charge Energy',
            game_text='Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Vibration',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)
