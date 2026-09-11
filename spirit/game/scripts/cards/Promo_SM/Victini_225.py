from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34173854-dcf1-56d4-8ed1-ab6bf1203c2e',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name',
    display_name='Victini',
    searchable_by=['Victini', 'Basic', 'Victini'],
    subtypes=['Basic'],
    collector_number=225,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=494,
    abilities=[
        Attack(
            title='Victory Sign',
            game_text='Search your deck for up to 2 basic Energy cards of different types and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
