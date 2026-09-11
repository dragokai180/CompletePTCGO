from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='535a151d-0ffc-5327-8c20-ceb20abfff52',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name',
    display_name='Bulbasaur',
    searchable_by=['Bulbasaur', 'Basic', 'Bulbasaur'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1,
    abilities=[
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
