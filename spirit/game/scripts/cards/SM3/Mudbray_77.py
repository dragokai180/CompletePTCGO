from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='11bf7331-6e3d-5403-a5e7-a23612b44705',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name',
    display_name='Mudbray',
    searchable_by=['Mudbray', 'Basic', 'Mudbray'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=749,
    abilities=[
        Attack(
            title='Stomp',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
