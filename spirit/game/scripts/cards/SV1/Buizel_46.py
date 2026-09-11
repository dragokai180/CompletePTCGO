from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa153920-dde6-5c29-b581-ab36f0713780',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    display_name='Buizel',
    searchable_by=['Buizel', 'Basic', 'Buizel'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=418,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Razor Fin',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
