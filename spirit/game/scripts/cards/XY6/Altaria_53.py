from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4ab5c463-ea70-5a01-b14b-e3a412aeaaef',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name',
    display_name='Altaria',
    searchable_by=['Altaria', 'Stage 1', 'Altaria'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    family_id=333,
    abilities=[
        Attack(
            title='Song of Echoes',
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Midnight Eyes',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
