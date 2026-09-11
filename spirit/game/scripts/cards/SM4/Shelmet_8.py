from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='20d92d6b-7f1e-509a-99f6-dff5888184f3',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name',
    display_name='Shelmet',
    searchable_by=['Shelmet', 'Basic', 'Shelmet'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=616,
    abilities=[
        Attack(
            title='Absorb',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
