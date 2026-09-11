from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='845c743e-7f31-5e26-8869-586f36daea1d',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name',
    display_name='Zangoose',
    searchable_by=['Zangoose', 'Basic', 'Zangoose'],
    subtypes=['Basic'],
    collector_number=132,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=335,
    abilities=[
        Attack(
            title='Head Hunt',
            game_text='Look at the top 6 cards of your deck, reveal any number of Pokémon you find there, and put them into your hand. Discard the other cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
