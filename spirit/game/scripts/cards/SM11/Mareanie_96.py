from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ff412bd3-abe9-510a-918b-760dab8d17b1',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    display_name='Mareanie',
    searchable_by=['Mareanie', 'Basic', 'Mareanie'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=747,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
