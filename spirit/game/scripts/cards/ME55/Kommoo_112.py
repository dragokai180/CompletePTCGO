from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79816a93-4991-5371-bb5d-4e3bdbad345b',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name',
    display_name='Kommo-o',
    searchable_by=['Kommo-o', 'Stage 2', 'Kommoo'],
    subtypes=['Stage 2'],
    collector_number=112,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name',
    family_id=782,
    abilities=[
        Attack(
            title='Blazing Uppercut',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=250,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
