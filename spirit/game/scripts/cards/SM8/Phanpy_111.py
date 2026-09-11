from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c69d89d0-4c0e-5f98-ae1e-9ac4e7085875',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    display_name='Phanpy',
    searchable_by=['Phanpy', 'Basic', 'Phanpy'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=231,
    abilities=[
        Attack(
            title='Last Resort',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
