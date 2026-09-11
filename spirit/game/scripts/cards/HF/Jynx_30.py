from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea7cf228-cfed-5574-b68c-f761314af144',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name',
    display_name='Jynx',
    searchable_by=['Jynx', 'Basic', 'Jynx'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=124,
    abilities=[
        Attack(
            title='Slap',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Lovely Kiss',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
