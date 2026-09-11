from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae832917-df2d-50fd-ab7b-96dbca884632',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    display_name='Rhyhorn',
    searchable_by=['Rhyhorn', 'Basic', 'Rhyhorn'],
    subtypes=['Basic'],
    collector_number=93,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=111,
    abilities=[
        Attack(
            title='Horn Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Boulder Crush',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
