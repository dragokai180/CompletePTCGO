from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a8a8826-9f09-53ea-beeb-3302a975edbe',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    display_name='Pawniard',
    searchable_by=['Pawniard', 'Basic', 'Pawniard'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=624,
    abilities=[
        Attack(
            title='Cut Down',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Metal Claw',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
