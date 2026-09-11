from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c5ea2b81-d875-5956-b579-edd8a4fb5053',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name',
    display_name='Popplio',
    searchable_by=['Popplio', 'Basic', 'Popplio'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=728,
    abilities=[
        Attack(
            title='Disarming Voice',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
