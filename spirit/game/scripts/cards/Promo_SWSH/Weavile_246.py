from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='188536ac-3d21-586e-b12e-a653ae21cdca',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name',
    display_name='Weavile',
    searchable_by=['Weavile', 'Stage 1', 'Weavile'],
    subtypes=['Stage 1'],
    collector_number=246,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH246'}},
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name',
    family_id=215,
    abilities=[
        Attack(
            title='Pursuit Claw',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon for each damage counter on that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
