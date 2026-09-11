from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b848656-32e2-5118-9b69-c70c2c56f6db',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name',
    display_name='Lugia',
    searchable_by=['Lugia', 'Basic', 'Lugia'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title='Linear Attack',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
