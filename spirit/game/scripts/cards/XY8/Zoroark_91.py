from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    stand_in, stand_in_condition,
)


card = PokemonCardDef(
    guid='ed2b8872-2b39-5033-9704-5f509031b197',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name',
    display_name='Zoroark',
    searchable_by=['Zoroark', 'Stage 1', 'Zoroark'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name',
    family_id=570,
    abilities=[
        Ability(
            title='Stand In',
            game_text='Once during your turn (before your attack), if this Pokémon is on your Bench, you may switch this Pokémon with your Active Pokémon.',
            effect=stand_in,
            condition=stand_in_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Mind Jack',
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
