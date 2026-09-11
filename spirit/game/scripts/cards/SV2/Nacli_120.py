from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dc0ddd44-e20a-5d14-af8e-5a12d838b082',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name',
    display_name='Nacli',
    searchable_by=['Nacli', 'Basic', 'Nacli'],
    subtypes=['Basic'],
    collector_number=120,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=932,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
