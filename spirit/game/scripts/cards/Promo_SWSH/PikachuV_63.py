from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c5a9168-e8e1-5cee-820d-1cecd09b7234',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name',
    display_name='Pikachu V',
    searchable_by=['Pikachu V', 'Basic', 'V', 'PikachuV'],
    subtypes=['Basic', 'V'],
    collector_number=63,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH063'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Pika Ball',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title='Circle Circuit',
            game_text='This attack does 30 damage for each of your Benched Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
