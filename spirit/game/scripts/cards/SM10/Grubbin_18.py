from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a64627b2-85d7-531a-a58a-372a8a26bba5',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name',
    display_name='Grubbin',
    searchable_by=['Grubbin', 'Basic', 'Grubbin'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=736,
    abilities=[
        Attack(
            title='Electrical Signal',
            game_text='Search your deck for up to 2 Lightning Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
