from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0017df96-540e-50e7-b0ea-9a799ebce70c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name',
    display_name='Gimmighoul',
    searchable_by=['Gimmighoul', 'Basic', 'Gimmighoul'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=999,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
