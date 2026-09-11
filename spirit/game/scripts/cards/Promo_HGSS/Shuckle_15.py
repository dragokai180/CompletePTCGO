from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01fdbb24-a700-5cf7-8b8e-735d5a8a81c3',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name',
    display_name='Shuckle',
    searchable_by=['Shuckle', 'Basic', 'Shuckle'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS15'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=213,
    abilities=[
        Ability(
            title='Fermenting Liquid',
            game_text='Whenever you attach an Energy card from your hand to Shuckle, draw a card.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Whenever you attach an Energy card from your hand to Shuckle, draw a card.'),
        ),
        Attack(
            title='Shell Stunner',
            game_text="Flip a coin. If heads, prevent all damage done to Shuckle by attacks during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
