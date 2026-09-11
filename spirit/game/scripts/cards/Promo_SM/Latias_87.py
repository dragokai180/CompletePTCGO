from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78602eea-0ffe-5207-bd42-408cff16bb51',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name',
    display_name='Latias',
    searchable_by=['Latias', 'Basic', 'Latias'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=380,
    abilities=[
        Ability(
            title='Flight Support',
            game_text='Your Latios in play have no Retreat Cost.',
            passive=standard_passive('Your Latios in play have no Retreat Cost.'),
        ),
        Attack(
            title='Misty Gale',
            game_text='Heal 30 damage from each of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
