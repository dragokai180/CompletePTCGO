from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5dae221b-37bb-59ac-a7af-1e236dd95f72',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name',
    display_name='Vaporeon',
    searchable_by=['Vaporeon', 'Stage 1', 'Vaporeon'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH072'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Watery Shroud',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 20 more damage for each Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
