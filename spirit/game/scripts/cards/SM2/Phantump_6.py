from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a029f3a7-b7cb-5cb5-8f57-2708f02c5b20',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    display_name='Phantump',
    searchable_by=['Phantump', 'Basic', 'Phantump'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=708,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Confuse Ray',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
