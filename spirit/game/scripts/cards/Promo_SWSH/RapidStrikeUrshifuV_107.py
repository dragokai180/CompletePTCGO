from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9c95cd16-ec42-5515-ab43-8a0985282199',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuV.Name',
    display_name='Rapid Strike Urshifu V',
    searchable_by=['Rapid Strike Urshifu V', 'Basic', 'V', 'Rapid Strike', 'RapidStrikeUrshifuV'],
    subtypes=['Basic', 'V', 'Rapid Strike'],
    collector_number=107,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH107'}},
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=892,
    abilities=[
        Attack(
            title='Spiral Kick',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Sonic Legs',
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
