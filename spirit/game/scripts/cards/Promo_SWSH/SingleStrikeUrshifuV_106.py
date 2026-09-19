from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da6ccfe9-a524-5459-a4f7-2847b38e893c',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuV.Name',
    display_name='Single Strike Urshifu V',
    searchable_by=['Single Strike Urshifu V', 'Basic', 'V', 'Single Strike', 'SingleStrikeUrshifuV'],
    subtypes=['Basic', 'V', 'Single Strike'],
    collector_number=106,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH106'}},
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=892,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title='Brawny Knuckle',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
