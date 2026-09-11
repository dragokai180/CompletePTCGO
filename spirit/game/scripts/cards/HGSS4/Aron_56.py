from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15b2d8b9-720f-5a11-a2f4-b3ca4d5b709b',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name',
    display_name='Aron',
    searchable_by=['Aron', 'Basic', 'Aron'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=304,
    abilities=[
        Attack(
            title='Mountain Eater',
            game_text='Discard the top card of your deck. Then, remove 2 damage counters from Aron.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Confront',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
