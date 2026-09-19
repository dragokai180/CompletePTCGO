from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6bb40458-717e-5571-866a-ae3d0f8dd7a1',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name',
    display_name='Galarian Obstagoon',
    searchable_by=['Galarian Obstagoon', 'Stage 2', 'GalarianObstagoon'],
    subtypes=['Stage 2'],
    collector_number=193,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH193'}},
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name',
    family_id=263,
    abilities=[
        Attack(
            title='Rampaging Kick',
            game_text='Discard 2 Darkness Energy from this Pokémon.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
