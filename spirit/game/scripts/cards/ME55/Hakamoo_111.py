from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58c874c9-355d-520e-aaed-e4634f8bffbf',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name',
    display_name='Hakamo-o',
    searchable_by=['Hakamo-o', 'Stage 1', 'Hakamoo'],
    subtypes=['Stage 1'],
    collector_number=111,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name',
    family_id=782,
    abilities=[
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
