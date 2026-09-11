from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e03e962-4370-56e9-b557-4962cddaeadc',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name',
    display_name='Grumpig',
    searchable_by=['Grumpig', 'Stage 1', 'Grumpig'],
    subtypes=['Stage 1'],
    collector_number=50,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    family_id=325,
    abilities=[
        Attack(
            title='Tricky Steps',
            game_text="You may move an Energy attached to your opponent's Active Pokémon to 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
