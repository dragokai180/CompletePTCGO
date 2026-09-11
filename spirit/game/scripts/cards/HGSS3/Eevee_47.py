from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e615c68-023d-5454-9687-ac7a8eb2d62d',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    display_name='Eevee',
    searchable_by=['Eevee', 'Basic', 'Eevee'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
