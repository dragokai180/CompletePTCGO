from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9d8a061d-0664-5643-8990-f565e02a83dc',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DrampaGX.Name',
    display_name='Drampa-GX',
    searchable_by=['Drampa-GX', 'Basic', 'GX', 'DrampaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=115,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=780,
    abilities=[
        Attack(
            title='Righteous Edge',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Berserk',
            game_text='If your Benched Pokémon have any damage counters on them, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Big Wheel-GX',
            game_text="Shuffle your hand into your deck. Then, draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
