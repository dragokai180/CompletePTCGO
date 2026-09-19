from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f386cd3e-78d4-572d-aed1-72ec2454a1b3',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name',
    display_name='Pikachu V',
    searchable_by=['Pikachu V', 'Basic', 'V', 'PikachuV'],
    subtypes=['Basic', 'V'],
    collector_number=285,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH285'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Pika Drive',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
