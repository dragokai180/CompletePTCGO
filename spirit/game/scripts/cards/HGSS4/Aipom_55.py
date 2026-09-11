from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5c04711e-aade-5198-9332-5943af17892a',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name',
    display_name='Aipom',
    searchable_by=['Aipom', 'Basic', 'Aipom'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=190,
    abilities=[
        Attack(
            title='Imitate',
            game_text='Draw cards until you have the same number of cards in your hand as your opponent.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
