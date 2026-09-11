from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d919bf7e-5bba-5392-8180-23395a18f296',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name',
    display_name='Manaphy',
    searchable_by=['Manaphy', 'Basic', 'Manaphy'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=490,
    abilities=[
        Attack(
            title='Deep Sea Swirl',
            game_text='Shuffle your hand into your deck. Then, draw 6 cards.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Life Saver',
            game_text='Put 2 Water Pokémon from your discard pile into your hand.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
