from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85f24c50-8eb8-5670-b099-2a984460eb37',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name',
    display_name='Mewtwo-EX',
    searchable_by=['Mewtwo-EX', 'Basic', 'EX', 'MewtwoEX'],
    subtypes=['Basic', 'EX'],
    collector_number=61,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Photon Wave',
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 30 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Psyburn',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
