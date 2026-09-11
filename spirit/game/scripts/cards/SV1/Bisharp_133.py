from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a334a64-e5bb-5f93-ba1f-461bfe222272',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name',
    display_name='Bisharp',
    searchable_by=['Bisharp', 'Stage 1', 'Bisharp'],
    subtypes=['Stage 1'],
    collector_number=133,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    family_id=624,
    abilities=[
        Attack(
            title='Dark Cutter',
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title='Double-Edged Slash',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
