from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='130c0699-441c-56c1-8e4a-f9ff321fea6d',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KyogreGroudonLEGEND.Name',
    display_name='Kyogre & Groudon LEGEND',
    searchable_by=['Kyogre & Groudon LEGEND', 'LEGEND', 'KyogreGroudonLEGEND'],
    subtypes=['LEGEND'],
    collector_number=87,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=150,
    elements=[PokemonTypes.WATER, PokemonTypes.FIGHTING],
    stage=PokemonStage.LEGEND,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Attack(
            title='Mega Tidal Wave',
            game_text="Discard the top 5 cards from your opponent's deck. This attack does 30 damage times the number of Energy cards you discarded to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Massive Eruption',
            game_text='Discard the top 5 cards from your deck. This attack does 100 damage times the number of Energy cards you discarded.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
