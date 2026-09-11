from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6385da56-33ac-5bdd-936c-c5dc65d2102b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    display_name='Drifloon',
    searchable_by=['Drifloon', 'Basic', 'Drifloon'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=425,
    abilities=[
        Attack(
            title='Gust',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
        Attack(
            title='Balloon Blast',
            game_text='This attack does 30 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
