from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dabd30f0-555d-56ee-8f6c-bb0038ef00ca',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    display_name='Surskit',
    searchable_by=['Surskit', 'Basic', 'Surskit'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=283,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
