from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f854227e-2a59-5373-b613-15800aba454b',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name',
    display_name='Yanmega',
    searchable_by=['Yanmega', 'Stage 1', 'Yanmega'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    family_id=193,
    abilities=[
        Attack(
            title='Windfall',
            game_text='Shuffle your hand into your deck. Then, draw 6 cards.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surprise Strike',
            game_text='If this Pokémon was on the Bench and became your Active Pokémon this turn, this attack does 50 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
