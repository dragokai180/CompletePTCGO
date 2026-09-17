from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3c04c05-175a-5f00-a656-f3c371febeba',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name',
    display_name='Comfey',
    searchable_by=['Comfey', 'Basic', 'Comfey'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=764,
    abilities=[
        Attack(
            title='Comforting Aroma',
            game_text='Heal 80 damage from 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Magical Shot',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
