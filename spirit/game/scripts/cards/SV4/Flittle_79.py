from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f39ac260-65b9-5553-9a8f-9549cfa65bde',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    display_name='Flittle',
    searchable_by=['Flittle', 'Basic', 'Flittle'],
    subtypes=['Basic'],
    collector_number=79,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
