from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae0268e7-bd27-5ed7-a1e4-e55da91caaf9',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name',
    display_name='Shroodle',
    searchable_by=['Shroodle', 'Basic', 'Shroodle'],
    subtypes=['Basic'],
    collector_number=144,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=944,
    abilities=[
        Attack(
            title='Berry Search',
            game_text='Put a Basic Energy card from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scratch',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
