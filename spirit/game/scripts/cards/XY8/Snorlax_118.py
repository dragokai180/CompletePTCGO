from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b024088d-be48-56ff-be71-a375719abc86',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Snorlax'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Ability(
            title='Plump Body',
            game_text='Any damage done to this Pokémon by attacks is reduced by 30 (after applying Weakness and Resistance).',
            passive=standard_passive('Any damage done to this Pokémon by attacks is reduced by 30 (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
