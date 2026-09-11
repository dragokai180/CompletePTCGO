from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='60a98c57-1fdf-51ec-84f3-0011b3e9fa49',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name',
    display_name='Cacnea',
    searchable_by=['Cacnea', 'Basic', 'Cacnea'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=331,
    abilities=[
        Attack(
            title='Swagger',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
