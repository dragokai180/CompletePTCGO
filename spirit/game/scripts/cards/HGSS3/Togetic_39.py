from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9de1a1f4-b7c5-5426-a5f6-2dd9abdaf391',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    display_name='Togetic',
    searchable_by=['Togetic', 'Stage 1', 'Togetic'],
    subtypes=['Stage 1'],
    collector_number=39,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name',
    family_id=175,
    abilities=[
        Attack(
            title='Chase Up',
            game_text='Search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fly',
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage done to Togetic during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
