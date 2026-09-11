from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9d959e7d-5eb3-593c-af73-c99172a798fa',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name',
    display_name='Lycanroc',
    searchable_by=['Lycanroc', 'Stage 1', 'Lycanroc'],
    subtypes=['Stage 1'],
    collector_number=76,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    family_id=745,
    abilities=[
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Accelerock',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
