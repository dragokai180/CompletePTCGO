from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2ad779dd-96ab-55b4-8f1d-7cc9fb08c263',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name',
    display_name='Snivy',
    searchable_by=['Snivy', 'Basic', 'Snivy'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=495,
    abilities=[
        Attack(
            title='Blot',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
