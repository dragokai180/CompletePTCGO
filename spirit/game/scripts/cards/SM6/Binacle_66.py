from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='74d6152a-6ad9-58a3-84fe-b52eb69da57c',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name',
    display_name='Binacle',
    searchable_by=['Binacle', 'Basic', 'Binacle'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=688,
    abilities=[
        Attack(
            title='Allotment',
            game_text='Draw a card.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
