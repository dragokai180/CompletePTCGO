from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c66b28fc-94af-5de0-a6de-64a29c4b16a0',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name',
    display_name='Blitzle',
    searchable_by=['Blitzle', 'Basic', 'Blitzle'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=522,
    abilities=[
        Attack(
            title='Rear Kick',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Wild Charge',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
