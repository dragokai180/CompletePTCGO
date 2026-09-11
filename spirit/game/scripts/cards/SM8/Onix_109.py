from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1e2b0b65-879c-5c0b-ba72-0b300fe2921f',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    display_name='Onix',
    searchable_by=['Onix', 'Basic', 'Onix'],
    subtypes=['Basic'],
    collector_number=109,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=95,
    abilities=[
        Attack(
            title='Land Crush',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)
