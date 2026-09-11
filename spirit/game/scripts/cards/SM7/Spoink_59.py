from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7ffc5ec4-8c04-5633-aa50-29c2af0d9930',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name',
    display_name='Spoink',
    searchable_by=['Spoink', 'Basic', 'Spoink'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=325,
    abilities=[
        Attack(
            title='Bounce',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
