from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8652ef01-b9cd-5e02-b402-7242e6d17557',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    display_name='Kakuna',
    searchable_by=['Kakuna', 'Stage 1', 'Kakuna'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    family_id=13,
    abilities=[
        Ability(
            title='Cocoon Cover',
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=standard_passive("Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)"),
        ),
        Attack(
            title='Zzzt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
