from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3aaf97c-19ee-55ea-aa9a-89992752e706',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name',
    display_name='Bayleef',
    searchable_by=['Bayleef', 'Stage 1', 'Bayleef'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name',
    family_id=152,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
