from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='594d7486-3435-59d2-9598-409af885fd42',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TaurosGX.Name',
    display_name='Tauros-GX',
    searchable_by=['Tauros-GX', 'Basic', 'GX', 'TaurosGX'],
    subtypes=['Basic', 'GX'],
    collector_number=100,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title='Rage',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Horn Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title='Mad Bull-GX',
            game_text="This attack does 30 damage for each damage counter on this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
