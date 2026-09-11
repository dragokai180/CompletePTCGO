from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8acce9b4-cdc5-5333-a6e3-8f9e10410d48',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KingdraGX.Name',
    display_name='Kingdra-GX',
    searchable_by=['Kingdra-GX', 'Stage 2', 'GX', 'KingdraGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=155,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    family_id=230,
    abilities=[
        Attack(
            title='Hydro Pump',
            game_text='This attack does 50 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Reverse Thrust',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Maelstrom-GX',
            game_text="This attack does 40 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
