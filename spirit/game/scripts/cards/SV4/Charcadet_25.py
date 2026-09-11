from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c90e24bf-a7c4-5ac6-9dc9-c5213a78ce6d',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    display_name='Charcadet',
    searchable_by=['Charcadet', 'Basic', 'Charcadet'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=935,
    abilities=[
        Attack(
            title='Protect',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Magma Punch',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
