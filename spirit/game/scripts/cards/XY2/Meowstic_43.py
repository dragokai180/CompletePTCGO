from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f8ede0d6-57d6-561a-860c-fb90da5fcad6',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name',
    display_name='Meowstic',
    searchable_by=['Meowstic', 'Stage 1', 'Meowstic'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name',
    family_id=677,
    abilities=[
        Attack(
            title='Ear Influence',
            game_text="Move as many damage counters on your opponent's Pokémon as you like to any of your opponent's other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic',
            game_text="Does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
