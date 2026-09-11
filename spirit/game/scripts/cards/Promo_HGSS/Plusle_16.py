from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='714cbc7b-a356-5738-8f8c-ecad9407f161',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name',
    display_name='Plusle',
    searchable_by=['Plusle', 'Basic', 'Plusle'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS16'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=311,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thunder Jolt',
            game_text='Flip a coin. If tails, Plusle does 10 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
