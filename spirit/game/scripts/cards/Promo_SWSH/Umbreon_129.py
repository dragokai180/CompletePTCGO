from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b57eccd9-aa9e-504c-a0c6-362812a02a5d',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name',
    display_name='Umbreon',
    searchable_by=['Umbreon', 'Stage 1', 'Umbreon'],
    subtypes=['Stage 1'],
    collector_number=129,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH129'}},
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Blindside',
            game_text="This attack does 60 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Moon Mirage',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
