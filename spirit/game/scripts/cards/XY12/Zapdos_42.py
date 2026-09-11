from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8ffd306d-1f98-5e81-9702-eca49e9aa6f3',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name',
    display_name='Zapdos',
    searchable_by=['Zapdos', 'Basic', 'Zapdos'],
    subtypes=['Basic'],
    collector_number=42,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=145,
    abilities=[
        Attack(
            title='Thunder',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Thunderbolt',
            game_text='Discard all Energy attached to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 4},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
