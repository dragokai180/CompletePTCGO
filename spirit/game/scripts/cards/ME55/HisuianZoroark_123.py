from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a3d49065-be5b-54ff-9525-f4775680c3df',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroark.Name',
    display_name='Hisuian Zoroark',
    searchable_by=['Hisuian Zoroark', 'Stage 1', 'HisuianZoroark'],
    subtypes=['Stage 1'],
    collector_number=123,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name',
    family_id=570,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Swirling Resentment',
            game_text="Place damage counters on your opponent's Active Pokémon until its remaining HP is 50.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
