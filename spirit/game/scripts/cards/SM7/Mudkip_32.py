from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e6ce8a5-1bef-5d1b-8c44-626c575c3eb3',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name',
    display_name='Mudkip',
    searchable_by=['Mudkip', 'Basic', 'Mudkip'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=258,
    abilities=[
        Attack(
            title='Water Reserve',
            game_text='Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
