from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1718f66-4d78-5397-a715-9ec8f848f48a',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name',
    display_name='Kangaskhan',
    searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'],
    subtypes=['Basic'],
    collector_number=128,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Fast Evolution',
            game_text='Search your deck for up to 2 Evolution Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mega Punch',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
