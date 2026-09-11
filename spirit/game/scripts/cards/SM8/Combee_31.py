from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49926a94-9576-5868-a73d-90c870ef15ff',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    display_name='Combee',
    searchable_by=['Combee', 'Basic', 'Combee'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=415,
    abilities=[
        Attack(
            title='Bee March',
            game_text='Search your deck for up to 3 Combee and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
