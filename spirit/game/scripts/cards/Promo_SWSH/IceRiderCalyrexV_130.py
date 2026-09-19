from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='155c0d92-3d17-5343-9f96-36f41eeb6772',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name',
    display_name='Ice Rider Calyrex V',
    searchable_by=['Ice Rider Calyrex V', 'Basic', 'V', 'IceRiderCalyrexV'],
    subtypes=['Basic', 'V'],
    collector_number=130,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH130'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=898,
    abilities=[
        Attack(
            title='Blizzard',
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Frost Stamp',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
