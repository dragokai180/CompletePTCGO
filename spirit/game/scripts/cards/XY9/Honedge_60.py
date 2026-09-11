from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='75e56d49-5867-5c47-8a87-e3acf2203a7d',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    display_name='Honedge',
    searchable_by=['Honedge', 'Basic', 'Honedge'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Attack(
            title='Stab',
            game_text="Put 1 damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
