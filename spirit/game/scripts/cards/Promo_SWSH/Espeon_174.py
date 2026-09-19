from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7d93faf1-6b38-57ba-8034-240f1261cde1',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name',
    display_name='Espeon',
    searchable_by=['Espeon', 'Stage 1', 'Espeon'],
    subtypes=['Stage 1'],
    collector_number=174,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH174'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
