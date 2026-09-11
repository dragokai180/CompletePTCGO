from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1447143b-08cb-5bf7-8c00-022779e7fb64',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    display_name='Riolu',
    searchable_by=['Riolu', 'Basic', 'Riolu'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=447,
    abilities=[
        Attack(
            title='Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
