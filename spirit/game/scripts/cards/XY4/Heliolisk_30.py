from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cfa7d0a2-4c25-5e81-9f0a-3b6c9381ef6e',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name',
    display_name='Heliolisk',
    searchable_by=['Heliolisk', 'Stage 1', 'Heliolisk'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name',
    family_id=694,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title='Parabolic Spark',
            game_text='Discard as many Lightning Energy attached to your Pokémon as you like. This attack does 30 damage times the number of Energy cards you discarded.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
