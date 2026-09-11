from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a630362e-3388-54d6-8cb7-0b671f8ad161',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name',
    display_name='Raikou',
    searchable_by=['Raikou', 'Basic', 'Raikou'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Ability(
            title='Shining Body',
            game_text='If this Pokémon has any Lightning Energy attached to it, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).',
            passive=standard_passive('If this Pokémon has any Lightning Energy attached to it, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Thunder Lance',
            game_text='This attack does 20 more damage for each Lightning Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
