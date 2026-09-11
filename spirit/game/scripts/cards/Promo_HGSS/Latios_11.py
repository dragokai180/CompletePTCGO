from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='147b11ad-52cb-5dc7-a59a-16d59749d266',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name',
    display_name='Latios',
    searchable_by=['Latios', 'Basic', 'Latios'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'HGSS11'}},
    weakness_type=PokemonTypes.COLORLESS,
    weakness_amount=2,
    family_id=381,
    abilities=[
        Ability(
            title='Luster Float',
            game_text='If you have Latias in play, the Retreat Cost for Latios is 0.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('If you have Latias in play, the Retreat Cost for Latios is 0.'),
        ),
        Attack(
            title='Infinite Wing',
            game_text='Discard 2 Energy attached to Latios.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
