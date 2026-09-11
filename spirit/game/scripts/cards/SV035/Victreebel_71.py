from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc4db889-20d8-5ea5-97a3-dbdabb383b7d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name',
    display_name='Victreebel',
    searchable_by=['Victreebel', 'Stage 2', 'Victreebel'],
    subtypes=['Stage 2'],
    collector_number=71,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    family_id=69,
    abilities=[
        Attack(
            title='Spit Up',
            cost={PokemonTypes.GRASS: 1},
            damage=50,
        ),
        Attack(
            title='Slow-Acting Acid',
            game_text="At the end of your opponent's next turn, put 12 damage counters on the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
