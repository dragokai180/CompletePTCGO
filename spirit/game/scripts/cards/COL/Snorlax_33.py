from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b19c4ae-a77b-58c4-bb96-81fdcfde3894',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Snorlax'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Attack(
            title='Layabout',
            game_text="Remove all damage counters from Snorlax. Snorlax can't use Layabout during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Clomp Clomp Clobber',
            game_text='Put 1 Energy card attached to Snorlax in the Lost Zone.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
