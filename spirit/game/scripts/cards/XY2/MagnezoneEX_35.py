from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b57ccc0f-3d1c-5aa9-a472-7b486cb9b733',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneEX.Name',
    display_name='Magnezone-EX',
    searchable_by=['Magnezone-EX', 'Basic', 'EX', 'MagnezoneEX'],
    subtypes=['Basic', 'EX'],
    collector_number=35,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=462,
    abilities=[
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title='Dual Bullet',
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness or Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            effect=standard_attack,
        ),
    ],
)
