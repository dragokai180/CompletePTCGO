from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ebad119c-be6c-598b-b626-43ba1b5bf321',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name',
    display_name='Pikachu V',
    searchable_by=['Pikachu V', 'Basic', 'V', 'PikachuV'],
    subtypes=['Basic', 'V'],
    collector_number=143,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH143'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Volt Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=standard_attack,
        ),
    ],
)
