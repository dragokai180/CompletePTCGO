from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cda9e586-826a-5c56-85b5-cf6ae088eaf2',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name',
    display_name='Togekiss',
    searchable_by=['Togekiss', 'Stage 2', 'Togekiss'],
    subtypes=['Stage 2'],
    collector_number=9,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    family_id=175,
    abilities=[
        Attack(
            title='Blessed Wings',
            game_text='Remove all damage counters from each of your Pokémon. Shuffle Togekiss and all cards attached to it back into your deck.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Air Cutter',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
