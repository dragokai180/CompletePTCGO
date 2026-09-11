from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2ce95612-967f-54d3-b171-6f9b3e036004',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name',
    display_name='Volbeat',
    searchable_by=['Volbeat', 'Basic', 'Volbeat'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=313,
    abilities=[
        Attack(
            title='Pheromone Catch',
            game_text='If your Illumise used Pheromone Signals during your last turn, this attack does 100 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
