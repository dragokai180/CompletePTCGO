from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c42c93c-d046-502b-b35a-13df015d1cc7',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    display_name='Weedle',
    searchable_by=['Weedle', 'Basic', 'Weedle'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=13,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
