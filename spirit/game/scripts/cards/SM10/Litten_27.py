from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='866dd400-76f4-5062-82fd-077c50ac22b9',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    display_name='Litten',
    searchable_by=['Litten', 'Basic', 'Litten'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=725,
    abilities=[
        Attack(
            title='Caturday',
            game_text='Draw a card. If you do, this Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Big Bite',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
