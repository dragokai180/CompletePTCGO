from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='347c49d2-db94-51d7-bfe4-6c685660c8f0',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    display_name='Graveler',
    searchable_by=['Graveler', 'Stage 1', 'Graveler'],
    subtypes=['Stage 1'],
    collector_number=46,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
