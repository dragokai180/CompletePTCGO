from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='98dfccbd-54a7-5347-9c8e-3da380b572a2',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name',
    display_name='Bergmite',
    searchable_by=['Bergmite', 'Basic', 'Bergmite'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=712,
    abilities=[
        Attack(
            title='Ice Block',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
