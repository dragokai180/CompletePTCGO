from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dbb58496-4dd2-51b5-884d-02a4d932e654',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name',
    display_name='Glaceon',
    searchable_by=['Glaceon', 'Stage 1', 'Glaceon'],
    subtypes=['Stage 1'],
    collector_number=192,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH192'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Hail',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Frosty Typhoon',
            game_text="During your next turn, this Pokémon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
