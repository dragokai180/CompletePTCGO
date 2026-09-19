from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62e71254-0ed4-5421-8ebe-8cce467dba86',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EeveeV.Name',
    display_name='Eevee V',
    searchable_by=['Eevee V', 'Basic', 'V', 'EeveeV'],
    subtypes=['Basic', 'V'],
    collector_number=65,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH065'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Brave Buddies',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 80 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
