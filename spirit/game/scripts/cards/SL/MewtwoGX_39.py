from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b31a1fbc-cb6f-5a18-a051-bce4fe51c345',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoGX.Name',
    display_name='Mewtwo-GX',
    searchable_by=['Mewtwo-GX', 'Basic', 'GX', 'MewtwoGX'],
    subtypes=['Basic', 'GX'],
    collector_number=39,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Full Burst',
            game_text='This attack does 30 damage times the amount of Energy attached to this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Super Absorption',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Psystrike-GX',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=200,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
