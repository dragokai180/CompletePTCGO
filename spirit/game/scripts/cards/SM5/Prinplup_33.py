from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85f5c6a6-c8f4-55ba-8998-a79ad045ac13',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name',
    display_name='Prinplup',
    searchable_by=['Prinplup', 'Stage 1', 'Prinplup'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name',
    family_id=393,
    abilities=[
        Attack(
            title='Bubble Beam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
