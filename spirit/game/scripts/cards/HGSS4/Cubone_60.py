from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d677e96-ce6c-5ad4-9642-a74f61f25dbb',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    display_name='Cubone',
    searchable_by=['Cubone', 'Basic', 'Cubone'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=104,
    abilities=[
        Ability(
            title='Lonely Bone',
            game_text="Any damage done to Cubone by your opponent's attacks is reduced by 20 for each Marowak in your discard pile (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            effect=standard_ability,
        ),
        Attack(
            title='Bone Rush',
            game_text='Flip a coin until you get tails. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
