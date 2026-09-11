from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e9af8ac-c023-5caa-a614-6d33d7d4220b',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name',
    display_name='Sableye',
    searchable_by=['Sableye', 'Basic', 'Sableye'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title='Bewitching Eyes',
            game_text="Choose a Supporter card from your opponent's discard pile and use it as the effect of this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Furtive Drop',
            game_text="Put 3 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
