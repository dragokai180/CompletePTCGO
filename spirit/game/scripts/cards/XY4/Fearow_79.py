from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b2103273-2533-5b76-bf40-e8f99d4fa56e',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name',
    display_name='Fearow',
    searchable_by=['Fearow', 'Stage 1', 'Fearow'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    family_id=21,
    abilities=[
        Attack(
            title='Fly',
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Drill Peck',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
