from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c45e3869-44d4-5098-84f0-f3b4a8cb2c29',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    display_name='Toxel',
    searchable_by=['Toxel', 'Basic', 'Toxel'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=848,
    abilities=[
        Attack(
            title='Slight Intrusion',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
