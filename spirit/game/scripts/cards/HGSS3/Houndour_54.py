from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b4c3fd15-ee54-5dab-ab59-bbf064b6c8c0',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    display_name='Houndour',
    searchable_by=['Houndour', 'Basic', 'Houndour'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=228,
    abilities=[
        Attack(
            title='Jump On',
            game_text='Flip a coin. If heads, this attack does 10 damage plus 10 more damage.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
