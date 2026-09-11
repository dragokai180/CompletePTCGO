from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af7a3d84-a33e-5cf9-ba1c-fa11d5b42cd3',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name',
    display_name='Beartic',
    searchable_by=['Beartic', 'Stage 1', 'Beartic'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name',
    family_id=613,
    abilities=[
        Attack(
            title='Igloo Hold',
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Mountain Drop',
            game_text='If there is any Stadium card in play, this attack does 40 more damage.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
