from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f717350e-02ef-5872-8b9d-7029e14e86cf',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name',
    display_name='Orbeetle',
    searchable_by=['Orbeetle', 'Stage 2', 'Orbeetle'],
    subtypes=['Stage 2'],
    collector_number=12,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name',
    family_id=824,
    abilities=[
        Attack(
            title='Satellite Beam',
            game_text="This attack does 30 damage for each Energy card in your opponent's discard pile.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Brain Shake',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
