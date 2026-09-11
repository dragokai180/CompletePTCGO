from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb8ee538-8659-505f-993f-f5339c2946e6',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MewEX.Name',
    display_name='Mew-EX',
    searchable_by=['Mew-EX', 'Basic', 'EX', 'MewEX'],
    subtypes=['Basic', 'EX'],
    collector_number=126,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=151,
    abilities=[
        Ability(
            title='Versatile',
            game_text="This Pokémon can use the attacks of any Pokémon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            passive=standard_passive("This Pokémon can use the attacks of any Pokémon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)"),
        ),
        Attack(
            title='Replace',
            game_text='Move as many Energy attached to your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
