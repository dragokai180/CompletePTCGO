from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d21b160c-1305-5cfa-955e-d2f590821f9e',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name',
    display_name='Ferrothorn',
    searchable_by=['Ferrothorn', 'Stage 1', 'Ferrothorn'],
    subtypes=['Stage 1'],
    collector_number=104,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name',
    family_id=598,
    abilities=[
        Attack(
            title='Spike Sting',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Kaboom Needles',
            game_text="This attack does 50 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) This Pokémon also does 130 damage to itself.",
            cost={PokemonTypes.METAL: 2},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
