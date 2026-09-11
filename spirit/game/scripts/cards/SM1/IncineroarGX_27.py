from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e07a9ef-f65b-5df6-85f3-27adc80f79eb',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarGX.Name',
    display_name='Incineroar-GX',
    searchable_by=['Incineroar-GX', 'Stage 2', 'GX', 'IncineroarGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=27,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name',
    family_id=725,
    abilities=[
        Attack(
            title='Hustling Strike',
            game_text='This attack does 20 more damage for each of your Benched Fire Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Tiger Swing',
            game_text='Flip 2 coins. This attack does 50 more damage for each heads.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Burning Slam-GX',
            game_text="Your opponent's Active Pokémon is now Burned. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
