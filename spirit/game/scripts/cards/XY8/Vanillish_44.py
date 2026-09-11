from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ce0f4f0-749f-5595-a00c-0a29276645e4',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name',
    display_name='Vanillish',
    searchable_by=['Vanillish', 'Stage 1', 'Vanillish'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name',
    family_id=582,
    abilities=[
        Attack(
            title='Ice Edge',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Icy Wind',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
