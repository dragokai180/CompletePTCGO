from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='64653805-6148-52eb-8fb9-45f594afdfa5',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    display_name='Electabuzz',
    searchable_by=['Electabuzz', 'Basic', 'Electabuzz'],
    subtypes=['Basic'],
    collector_number=125,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=125,
    abilities=[
        Attack(
            title='Electro Combo',
            game_text='If Magmar is on your Bench, this attack does 40 more damage.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Light Punch',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
