from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5526f1ed-6703-51bd-99f6-799dba3ee7b5',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PheromosaGX.Name',
    display_name='Pheromosa-GX',
    searchable_by=['Pheromosa-GX', 'Basic', 'GX', 'Ultra Beast', 'PheromosaGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=66,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=795,
    abilities=[
        Attack(
            title='Fast Raid',
            game_text='If you go first, you can use this attack on your first turn.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Cruel Spike',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Beauty-GX',
            game_text="This attack does 50 damage for each Prize card your opponent has taken. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
