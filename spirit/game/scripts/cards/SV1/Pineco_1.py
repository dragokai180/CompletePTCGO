from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7540b60e-6001-5760-981b-68633ed3d59c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    display_name='Pineco',
    searchable_by=['Pineco', 'Basic', 'Pineco'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=204,
    abilities=[
        Attack(
            title='Guard Press',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
