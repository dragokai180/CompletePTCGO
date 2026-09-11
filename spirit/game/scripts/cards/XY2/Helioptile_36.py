from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='11095e66-5047-5b3b-a1dd-9293122bd3df',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name',
    display_name='Helioptile',
    searchable_by=['Helioptile', 'Basic', 'Helioptile'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=694,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Destructive Beam',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
