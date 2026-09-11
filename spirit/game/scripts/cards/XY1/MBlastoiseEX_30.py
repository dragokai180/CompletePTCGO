from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01134ed3-152d-5b6f-a117-d32677995ef2',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MBlastoiseEX.Name',
    display_name='M Blastoise-EX',
    searchable_by=['M Blastoise-EX', 'MEGA', 'EX', 'MBlastoiseEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=30,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name',
    family_id=9,
    abilities=[
        Attack(
            title='Hydro Bombard',
            game_text="This attack does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
