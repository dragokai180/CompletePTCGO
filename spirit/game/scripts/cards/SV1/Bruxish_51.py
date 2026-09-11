from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a89538b-0413-525f-ab8b-27dc54e3f048',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name',
    display_name='Bruxish',
    searchable_by=['Bruxish', 'Basic', 'Bruxish'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=779,
    abilities=[
        Attack(
            title='Vivid Charge',
            game_text='Search your deck for up to 3 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
