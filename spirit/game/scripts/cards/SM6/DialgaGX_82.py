from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f878b440-5e2f-5717-aeb8-f5c7b7620bf4',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DialgaGX.Name',
    display_name='Dialga-GX',
    searchable_by=['Dialga-GX', 'Basic', 'GX', 'DialgaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=82,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title='Overclock',
            game_text='Draw cards until you have 6 cards in your hand.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Shred',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Timeless-GX',
            game_text="Take another turn after this one. (Skip the between-turns step.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
