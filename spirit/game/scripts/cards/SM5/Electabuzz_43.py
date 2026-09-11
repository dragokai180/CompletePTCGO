from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ac58d2a-f797-5d78-a774-53a4cca052a8',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    display_name='Electabuzz',
    searchable_by=['Electabuzz', 'Basic', 'Electabuzz'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=125,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Thunder',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
