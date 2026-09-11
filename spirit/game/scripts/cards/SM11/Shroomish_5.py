from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7e43da9-ece1-5d05-92f3-af4de4bdadf0',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    display_name='Shroomish',
    searchable_by=['Shroomish', 'Basic', 'Shroomish'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=285,
    abilities=[
        Attack(
            title='Poison Powder',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
