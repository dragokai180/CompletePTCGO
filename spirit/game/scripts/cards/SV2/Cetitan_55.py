from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ddd1841-9903-5bf7-8c2e-a7e51a1ee59d',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name',
    display_name='Cetitan',
    searchable_by=['Cetitan', 'Stage 1', 'Cetitan'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    family_id=974,
    abilities=[
        Attack(
            title='Icicle Missile',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Special Horn',
            game_text='If this Pokémon has any Special Energy attached, this attack does 140 more damage.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
