from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8f00fde-92d7-5a84-8ebe-6f88d72ba02b',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name',
    display_name='Dolliv',
    searchable_by=['Dolliv', 'Stage 1', 'Dolliv'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name',
    family_id=928,
    abilities=[
        Attack(
            title='Sunny Wind',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
