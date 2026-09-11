from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5d26d39-3366-546f-964e-d4d839297b2f',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name',
    display_name='Armaldo',
    searchable_by=['Armaldo', 'Stage 1', 'Armaldo'],
    subtypes=['Stage 1'],
    collector_number=57,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name',
    family_id=347,
    abilities=[
        Attack(
            title='Rushing Water',
            game_text="Move an Energy from your opponent's Active Pokémon to 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Guard Claw',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
