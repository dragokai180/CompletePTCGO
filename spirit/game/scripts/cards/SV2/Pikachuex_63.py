from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='74e0da38-3bf3-5ce9-9ddd-cb1d422a6795',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name',
    display_name='Pikachu ex',
    searchable_by=['Pikachu ex', 'Basic', 'ex', 'Pikachuex'],
    subtypes=['Basic', 'ex'],
    collector_number=63,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Pika Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Dynamic Bolt',
            game_text='Flip a coin. If tails, discard all Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
