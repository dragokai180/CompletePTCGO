from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1d92f887-24ae-5a8d-8398-9e6a1d2eea2d',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    display_name='Phanpy',
    searchable_by=['Phanpy', 'Basic', 'Phanpy'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=231,
    abilities=[
        Ability(
            title='Ultra-Thick Skin',
            game_text='As long as Phanpy has Energy attached to it, any damage done to Phanpy by attacks is reduced by 10 (after applying Weakness and Resistance).',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Phanpy has Energy attached to it, any damage done to Phanpy by attacks is reduced by 10 (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Rock Smash',
            game_text='Flip a coin. If heads, this attack does 20 damage plus 10 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
