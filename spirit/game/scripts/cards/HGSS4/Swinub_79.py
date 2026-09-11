from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58f3b074-bcae-5b89-8971-53b3255842ec',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name',
    display_name='Swinub',
    searchable_by=['Swinub', 'Basic', 'Swinub'],
    subtypes=['Basic'],
    collector_number=79,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=220,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Ice Ball',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
