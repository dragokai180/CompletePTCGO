from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4aea8d6a-a828-5949-911e-f23405e70f05',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    display_name='Poliwhirl',
    searchable_by=['Poliwhirl', 'Stage 1', 'Poliwhirl'],
    subtypes=['Stage 1'],
    collector_number=61,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Frog Hop',
            game_text='Flip a coin. If heads, this attack does 60 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
