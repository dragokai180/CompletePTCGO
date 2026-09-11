from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b0a8223e-9738-5d00-a33a-aa696517e2ba',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name',
    display_name="Team Aqua's Sealeo",
    searchable_by=["Team Aqua's Sealeo", 'Stage 1', 'TeamAquasSealeo'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name',
    family_id=363,
    abilities=[
        Attack(
            title='Splatter',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hail Storm',
            game_text="If your opponent's Active Pokémon is a Team Magma Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
