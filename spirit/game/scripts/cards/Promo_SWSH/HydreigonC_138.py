from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4ba91de1-ad6b-5c88-bd90-d25f8665d2a5',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HydreigonC.Name',
    display_name='Hydreigon C',
    searchable_by=['Hydreigon C', 'Basic', 'SP', 'HydreigonC'],
    subtypes=['Basic', 'SP'],
    collector_number=138,
    set_code='Promo_SWSH',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH138'}},
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=635,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Berserker Blade',
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
