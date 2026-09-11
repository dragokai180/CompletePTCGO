from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5f8fb3c-a6a4-551f-a467-f1dc8066f9f7',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    display_name='Venonat',
    searchable_by=['Venonat', 'Basic', 'Venonat'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=48,
    abilities=[
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
