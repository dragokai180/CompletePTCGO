from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2bb121b8-bc37-502c-9c70-3cd58b4c6be3',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name',
    display_name='Meganium',
    searchable_by=['Meganium', 'Stage 2', 'Meganium'],
    subtypes=['Stage 2'],
    collector_number=26,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name',
    family_id=152,
    abilities=[
        Attack(
            title='Sleep Powder',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Giant Bloom',
            game_text='Remove 2 damage counters from Meganium.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
