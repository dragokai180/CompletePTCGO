from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0eccaa1-2b23-578f-95c1-b451bf090bda',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    display_name='Bellsprout',
    searchable_by=['Bellsprout', 'Basic', 'Bellsprout'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=69,
    abilities=[
        Attack(
            title='Cut',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Bind Down',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
