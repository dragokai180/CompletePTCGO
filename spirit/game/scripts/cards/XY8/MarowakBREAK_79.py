from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='498101c2-ba80-59d8-aee3-cfb5d8c34c21',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MarowakBREAK.Name',
    display_name='Marowak BREAK',
    searchable_by=['Marowak BREAK', 'BREAK', 'MarowakBREAK'],
    subtypes=['BREAK'],
    collector_number=79,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name',
    family_id=104,
    abilities=[
        Attack(
            title='Bone Revenge',
            game_text='This attack does 40 more damage for each Prize card your opponent has taken.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
