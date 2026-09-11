from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e85fb38e-7c65-5f44-9129-f19214f1ddf1',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name',
    display_name='Arctibax',
    searchable_by=['Arctibax', 'Stage 1', 'Arctibax'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name',
    family_id=996,
    abilities=[
        Attack(
            title='Sharp Fin',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Frost Smash',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
