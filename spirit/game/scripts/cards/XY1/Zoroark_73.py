from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='288f0410-9b74-5d31-847f-72d1fcb3dd7c',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name',
    display_name='Zoroark',
    searchable_by=['Zoroark', 'Stage 1', 'Zoroark'],
    subtypes=['Stage 1'],
    collector_number=73,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name',
    family_id=570,
    abilities=[
        Attack(
            title='Corner',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Night Claw',
            game_text='Flip a coin. If tails, discard 2 Energy attached to this Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
