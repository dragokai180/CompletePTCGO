from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eeb02153-a63e-5e13-925f-00e6ba4b0a6f',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name',
    display_name='Kricketune',
    searchable_by=['Kricketune', 'Stage 1', 'Kricketune'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name',
    family_id=401,
    abilities=[
        Attack(
            title='Screech',
            game_text='During your next turn, any damage done to the Defending Pokémon by attacks is increased by 60 (after applying Weakness and Resistance).',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)
