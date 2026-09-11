from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e769b294-6465-5725-8b84-47308d66c406',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name',
    display_name='Klink',
    searchable_by=['Klink', 'Basic', 'Klink'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=599,
    abilities=[
        Attack(
            title='Disorderly Flip',
            game_text='Flip 4 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
