from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0fa9c356-157f-5863-9ef8-0b2b36db10fd',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name',
    display_name='Heracross',
    searchable_by=['Heracross', 'Basic', 'Heracross'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Attack(
            title='Lunge Out',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Riled Horn',
            game_text='If your opponent has any TAG TEAM Pokémon in play, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
