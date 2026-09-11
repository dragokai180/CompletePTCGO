from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb07bfc0-1f94-59b3-a3ad-b31140e263b1',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name',
    display_name='Shedinja',
    searchable_by=['Shedinja', 'Stage 1', 'Shedinja'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name',
    family_id=290,
    abilities=[
        Attack(
            title='Cursed Rain',
            game_text="Put 1 damage counter on each of your opponent's Pokémon. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hopeless Scream',
            game_text='This attack does 50 damage times the number of damage counters on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
