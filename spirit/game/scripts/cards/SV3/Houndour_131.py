from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='421b43e8-1c9f-5a9a-ac2b-fc396cceb721',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    display_name='Houndour',
    searchable_by=['Houndour', 'Basic', 'Houndour'],
    subtypes=['Basic'],
    collector_number=131,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=228,
    abilities=[
        Attack(
            title='Coordinated Pack',
            game_text='For each of your Benched Houndour, search your deck for a Basic Darkness Energy card and attach it to that Houndour. Then, shuffle your deck.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Focus Fangs',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
