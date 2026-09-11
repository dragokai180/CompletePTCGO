from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ac1bd1c-5bf6-518b-87d7-1fd9dc547a03',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name',
    display_name='Sylveon',
    searchable_by=['Sylveon', 'Stage 1', 'Sylveon'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Curly Ribbon',
            game_text="Move an Energy attached to your opponent's Active Pokémon to 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Echoed Voice',
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
