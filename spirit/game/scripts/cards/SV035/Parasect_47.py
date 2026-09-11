from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e2b94ed2-eddd-593c-b3cf-a3a7c2a5f195',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name',
    display_name='Parasect',
    searchable_by=['Parasect', 'Stage 1', 'Parasect'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name',
    family_id=46,
    abilities=[
        Attack(
            title='Spread Filaments',
            game_text='Flip 2 coins. Search your deck for a number of Grass Pokémon up to the number of heads and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
