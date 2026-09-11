from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='272cd6f6-7156-5a73-9529-172ea92b38c4',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name',
    display_name='Golduck',
    searchable_by=['Golduck', 'Stage 1', 'Golduck'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    family_id=54,
    abilities=[
        Attack(
            title='Aquatic Rescue',
            game_text='Put up to 4 Pokémon from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Super Splash',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
