from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a88421a6-06aa-5d2c-8368-61d2aa3d6780',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name',
    display_name='Illumise',
    searchable_by=['Illumise', 'Basic', 'Illumise'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=314,
    abilities=[
        Attack(
            title='Pheromone Signals',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
