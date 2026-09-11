from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='906808ea-c4b0-5697-9d0e-38103089a2b9',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name',
    display_name='Liepard',
    searchable_by=['Liepard', 'Stage 1', 'Liepard'],
    subtypes=['Stage 1'],
    collector_number=115,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name',
    family_id=509,
    abilities=[
        Attack(
            title='Dishonest Swap',
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
