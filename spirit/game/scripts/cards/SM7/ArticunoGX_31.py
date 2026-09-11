from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3462e313-dfa4-5150-9e50-d114dcf0eeda',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ArticunoGX.Name',
    display_name='Articuno-GX',
    searchable_by=['Articuno-GX', 'Basic', 'GX', 'ArticunoGX'],
    subtypes=['Basic', 'GX'],
    collector_number=31,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=144,
    abilities=[
        Ability(
            title='Legendary Ascent',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may switch it with your Active Pokémon. If you do, move any number of Water Energy from your other Pokémon to this Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Ice Wing',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title='Cold Crush-GX',
            game_text="Discard all Energy from both Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
