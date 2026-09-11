from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46531862-b540-5974-ad37-a1e93d0f849c',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastrodon.Name',
    display_name='Gastrodon',
    searchable_by=['Gastrodon', 'Stage 1', 'Gastrodon'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name',
    family_id=422,
    abilities=[
        Attack(
            title='Sticky Shot',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
