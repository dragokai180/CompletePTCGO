from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee8df031-bc12-5795-a3d0-ff67484be0d4',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name',
    display_name='Oricorio',
    searchable_by=['Oricorio', 'Basic', 'Oricorio'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=741,
    abilities=[
        Attack(
            title='Passionate Dance',
            game_text='Search your deck for up to 3 Basic Fire Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Kindle',
            game_text="Discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
