from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d3ebc61-dc4f-540f-9859-062aa26fc0bf',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    display_name='Jigglypuff',
    searchable_by=['Jigglypuff', 'Basic', 'Jigglypuff'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=39,
    abilities=[
        Attack(
            title='Healing Melody',
            game_text='Heal 10 damage from each of your Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
