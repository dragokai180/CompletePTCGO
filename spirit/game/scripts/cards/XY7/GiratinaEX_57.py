from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8fedae6-d247-52f3-b2a3-cf24bbc16c3e',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaEX.Name',
    display_name='Giratina-EX',
    searchable_by=['Giratina-EX', 'Basic', 'EX', 'GiratinaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=57,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=487,
    abilities=[
        Ability(
            title='Renegade Pulse',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Mega Evolution Pokémon.",
            passive=standard_passive("Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Mega Evolution Pokémon."),
        ),
        Attack(
            title='Chaos Wheel',
            game_text="Your opponent can't play any Pokémon Tool, Special Energy, or Stadium cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
