from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a71c913-1447-5333-9c65-1fac4dbf6e78',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoGX.Name',
    display_name='Tapu Koko-GX',
    searchable_by=['Tapu Koko-GX', 'Basic', 'GX', 'TapuKokoGX'],
    subtypes=['Basic', 'GX'],
    collector_number=33,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=785,
    abilities=[
        Ability(
            title='Aero Trail',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may move any number of Lightning Energy from your other Pokémon to this Pokémon. If you do, switch this Pokémon with your Active Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Sky-High Claws',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title='Tapu Thunder-GX',
            game_text="This attack does 50 damage times the amount of Energy attached to all of your opponent's Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
