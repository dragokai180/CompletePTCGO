from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='277f5c0d-b9ff-57a9-aa58-b0001053908e',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RaikouSuicuneLEGEND.Name',
    display_name='Raikou & Suicune LEGEND',
    searchable_by=['Raikou & Suicune LEGEND', 'LEGEND', 'RaikouSuicuneLEGEND'],
    subtypes=['LEGEND'],
    collector_number=92,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=160,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.WATER],
    stage=PokemonStage.LEGEND,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=243,
    abilities=[
        Attack(
            title='Thunderbolt Spear',
            game_text="Raikou & Suicune LEGEND does 50 damage to itself and don't apply Weakness to this damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Aurora Gain',
            game_text='Remove 5 damage counters from Raikou & Suicune LEGEND.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
