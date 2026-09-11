from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0e63f78d-37c7-5f65-9671-aba85c7bcf13',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name',
    display_name='Shelgon',
    searchable_by=['Shelgon', 'Stage 1', 'Shelgon'],
    subtypes=['Stage 1'],
    collector_number=56,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name',
    family_id=371,
    abilities=[
        Ability(
            title='Exoskeleton',
            game_text='Any damage done to this Pokémon by attacks is reduced by 10 (after applying Weakness and Resistance).',
            passive=standard_passive('Any damage done to this Pokémon by attacks is reduced by 10 (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
