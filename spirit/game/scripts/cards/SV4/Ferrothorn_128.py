from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24ab0216-e7f3-53cd-86d4-c9dca5b90a20',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name',
    display_name='Ferrothorn',
    searchable_by=['Ferrothorn', 'Stage 1', 'Ferrothorn'],
    subtypes=['Stage 1'],
    collector_number=128,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name',
    family_id=597,
    abilities=[
        Ability(
            title='Exoskeleton',
            game_text='This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Spinning Needles',
            game_text="During your next turn, this Pokémon's Spinning Needles attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
