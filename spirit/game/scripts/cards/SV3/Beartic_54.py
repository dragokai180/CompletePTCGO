from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5198a5fe-8a4e-5e0b-b0c2-e9806688af07',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name',
    display_name='Beartic',
    searchable_by=['Beartic', 'Stage 1', 'Beartic'],
    subtypes=['Stage 1'],
    collector_number=54,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name',
    family_id=613,
    abilities=[
        Attack(
            title='Icicle Punch',
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title='Frost Purge',
            game_text='Flip a coin. If tails, discard all Energy from this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
