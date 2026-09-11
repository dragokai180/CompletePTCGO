from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='961c5de5-9171-58cf-8d9b-fb48fef10354',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name',
    display_name='Silicobra',
    searchable_by=['Silicobra', 'Basic', 'Silicobra'],
    subtypes=['Basic'],
    collector_number=119,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=843,
    abilities=[
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
