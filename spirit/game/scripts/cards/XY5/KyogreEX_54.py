from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c36d0844-ac25-56a5-9970-0140752b644b',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name',
    display_name='Kyogre-EX',
    searchable_by=['Kyogre-EX', 'Basic', 'EX', 'KyogreEX'],
    subtypes=['Basic', 'EX'],
    collector_number=54,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Giant Whirlpool',
            game_text='Return 2 Water Energy attached to this Pokémon to your hand.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
