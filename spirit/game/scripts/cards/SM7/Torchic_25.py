from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33a81ed5-46d3-5728-a06d-39e8ed9de650',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    display_name='Torchic',
    searchable_by=['Torchic', 'Basic', 'Torchic'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=255,
    abilities=[
        Attack(
            title='Ember',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
