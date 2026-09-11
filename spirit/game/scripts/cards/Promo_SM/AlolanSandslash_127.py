from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f5caccac-bcd2-52e4-a490-7182b6b6afe7',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name',
    display_name='Alolan Sandslash',
    searchable_by=['Alolan Sandslash', 'Stage 1', 'AlolanSandslash'],
    subtypes=['Stage 1'],
    collector_number=127,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name',
    family_id=28,
    abilities=[
        Attack(
            title='Metal Claw',
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title='Tumbling Attack',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
