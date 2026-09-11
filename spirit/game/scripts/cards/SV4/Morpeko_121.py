from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8b859a80-2718-5717-9401-11e83d4f72ea',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name',
    display_name='Morpeko',
    searchable_by=['Morpeko', 'Basic', 'Morpeko'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=877,
    abilities=[
        Ability(
            title='In a Hungry Hurry',
            game_text='If this Pokémon has no Energy attached, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has no Energy attached, it has no Retreat Cost.'),
        ),
        Attack(
            title='Energizer Wheel',
            game_text='Move 2 Darkness Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
