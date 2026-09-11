from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fde8418-5e7e-5616-baa5-f27bdf2f2e25',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name',
    display_name='Poipole',
    searchable_by=['Poipole', 'Basic', 'Ultra Beast', 'Poipole'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=102,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=803,
    abilities=[
        Attack(
            title='Belt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Last Scene',
            game_text='If each player has exactly 1 Prize card remaining, this attack does 130 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
