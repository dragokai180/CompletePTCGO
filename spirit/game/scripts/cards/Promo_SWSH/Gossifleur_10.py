from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18641daa-8ef1-5f65-9ea8-c7d4e901a570',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name',
    display_name='Gossifleur',
    searchable_by=['Gossifleur', 'Basic', 'Gossifleur'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH010'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=829,
    abilities=[
        Attack(
            title='Sing',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
