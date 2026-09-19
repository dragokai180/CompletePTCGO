from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='57f36194-fa18-58fb-a43d-c845f81f0646',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseV.Name',
    display_name='Blastoise V',
    searchable_by=['Blastoise V', 'Basic', 'V', 'BlastoiseV'],
    subtypes=['Basic', 'V'],
    collector_number=101,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH101'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=9,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title='Torrential Cannon',
            game_text="During your next turn, this Pokémon can't use Torrential Cannon.",
            cost={PokemonTypes.WATER: 3},
            damage=200,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
