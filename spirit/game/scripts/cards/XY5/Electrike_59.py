from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ebeed981-b129-579c-99ca-8986f5c46c85',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name',
    display_name='Electrike',
    searchable_by=['Electrike', 'Basic', 'Electrike'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=309,
    abilities=[
        Attack(
            title='Charge',
            game_text='Search your deck for a Lightning Energy card and attach it to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
