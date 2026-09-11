from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='98cc31be-2d0b-5971-bbaf-e8e10e516ff7',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    display_name='Hoppip',
    searchable_by=['Hoppip', 'Basic', 'Hoppip'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=187,
    abilities=[
        Attack(
            title='Bounce',
            game_text='You may switch Hoppip with 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
