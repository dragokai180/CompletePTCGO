from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d9131076-28ef-5cce-95c1-da96081dbf7f',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name',
    display_name='Paras',
    searchable_by=['Paras', 'Basic', 'Paras'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=46,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Spore Ball',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
