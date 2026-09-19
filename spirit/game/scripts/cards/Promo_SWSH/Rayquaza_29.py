from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78f43849-987f-5bac-b546-de42026688d9',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name',
    display_name='Rayquaza',
    searchable_by=['Rayquaza', 'Basic', 'Rayquaza'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH029'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=384,
    abilities=[
        Attack(
            title='Jaw Lock',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Power Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
