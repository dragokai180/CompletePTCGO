from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe2b9c67-2df5-5c91-b6b7-b4f888f525b2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name',
    display_name='Volcanion',
    searchable_by=['Volcanion', 'Basic', 'Volcanion'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Attack(
            title='Dual Turbo',
            game_text='Choose up to 2 of your Benched Pokémon and attach a Basic Fire Energy card from your discard pile to each of them.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
