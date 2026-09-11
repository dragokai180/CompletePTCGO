from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='27014a60-c883-5c12-99f4-c91b43807f68',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name',
    display_name='Sharpedo',
    searchable_by=['Sharpedo', 'Stage 1', 'Sharpedo'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    family_id=318,
    abilities=[
        Attack(
            title='Aqua Impact',
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Jet Headbutt',
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
