from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ae53ab7-1745-5fee-8ecb-ca27cdc1c348',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HeatranGX.Name',
    display_name='Heatran-GX',
    searchable_by=['Heatran-GX', 'Basic', 'GX', 'HeatranGX'],
    subtypes=['Basic', 'GX'],
    collector_number=25,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=485,
    abilities=[
        Ability(
            title='Burning Road',
            game_text='Once during your turn, when this Pokémon moves from your Bench to become your Active Pokémon, you may move any number of Fire Energy from your other Pokémon to it.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Steaming Stomp',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title='Hot Burn-GX',
            game_text="This attack does 50 damage times the amount of Fire Energy attached to this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
