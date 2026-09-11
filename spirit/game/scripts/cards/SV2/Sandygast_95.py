from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='26cac367-5a44-5a90-af8b-32b3f7d00c14',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name',
    display_name='Sandygast',
    searchable_by=['Sandygast', 'Basic', 'Sandygast'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=769,
    abilities=[
        Attack(
            title='Mumble',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Mud Shot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
