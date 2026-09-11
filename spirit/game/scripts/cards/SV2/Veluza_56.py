from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c8efd52-eb85-5389-8d7d-5f3e3c271a76',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name',
    display_name='Veluza',
    searchable_by=['Veluza', 'Basic', 'Veluza'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=976,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Slim Screw',
            game_text='If you have no cards in your hand, this attack can be used for Water.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
