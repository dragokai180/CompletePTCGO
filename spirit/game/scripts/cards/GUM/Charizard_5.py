from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f879e45-c7fd-503c-813e-b54353af0a89',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name',
    display_name='Charizard',
    searchable_by=['Charizard', 'Stage 2', 'Charizard'],
    subtypes=['Stage 2'],
    collector_number=5,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=6,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title='Wild Tackle',
            game_text='This Pokémon does 50 damage to itself.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
