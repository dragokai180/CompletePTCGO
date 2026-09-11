from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fbfbe142-d21a-51cb-8ca8-4afbddb5a21e',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name',
    display_name='White Kyurem',
    searchable_by=['White Kyurem', 'Basic', 'WhiteKyurem'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Burning Icicles',
            game_text="If this Pokémon has any Fire Energy attached to it, this attack does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Blizzard Burn',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
