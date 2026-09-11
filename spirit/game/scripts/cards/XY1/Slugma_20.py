from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7912cdb9-b43d-55b9-ab24-5f8957055025',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    display_name='Slugma',
    searchable_by=['Slugma', 'Basic', 'Slugma'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=218,
    abilities=[
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
