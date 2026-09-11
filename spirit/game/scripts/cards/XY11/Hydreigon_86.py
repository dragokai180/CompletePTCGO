from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40fc8638-9dda-53c6-9000-0550b1a8eef6',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name',
    display_name='Hydreigon',
    searchable_by=['Hydreigon', 'Stage 2', 'Hydreigon'],
    subtypes=['Stage 2'],
    collector_number=86,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name',
    family_id=633,
    abilities=[
        Attack(
            title='Cruel Fang',
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 40 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Dark Burn',
            game_text='Discard as many Darkness Energy attached to your Pokémon as you like. This attack does 50 damage times the amount of Darkness Energy you discarded in this way.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
