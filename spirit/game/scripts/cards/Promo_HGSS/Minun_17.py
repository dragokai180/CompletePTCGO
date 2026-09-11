from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a452354-4b64-575c-af93-7821fc2c6ed8',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name',
    display_name='Minun',
    searchable_by=['Minun', 'Basic', 'Minun'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS17'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=312,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tag Team Boost',
            game_text='If Plusle is on your Bench, this attack does 10 damage plus 20 more damage.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
