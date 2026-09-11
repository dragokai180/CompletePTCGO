from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dca7c961-3437-5751-b00e-8cb866e29eb6',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GolisopodGX.Name',
    display_name='Golisopod-GX',
    searchable_by=['Golisopod-GX', 'Stage 1', 'GX', 'GolisopodGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=62,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    family_id=768,
    abilities=[
        Attack(
            title='First Impression',
            game_text='If this Pokémon was on the Bench and became your Active Pokémon this turn, this attack does 90 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Armor Press',
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
        Attack(
            title='Crossing Cut-GX',
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
