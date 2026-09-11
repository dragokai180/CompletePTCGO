from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9055f3e-a667-5fad-a81e-9eb3008bf513',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuFiniGX.Name',
    display_name='Tapu Fini-GX',
    searchable_by=['Tapu Fini-GX', 'Basic', 'GX', 'TapuFiniGX'],
    subtypes=['Basic', 'GX'],
    collector_number=133,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=788,
    abilities=[
        Attack(
            title='Aqua Ring',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Shot',
            game_text="Discard 2 Water Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness or Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tapu Storm-GX',
            game_text="Shuffle your opponent's Active Pokémon and all cards attached to it into their deck. If your opponent has no Benched Pokémon, this attack does nothing. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
