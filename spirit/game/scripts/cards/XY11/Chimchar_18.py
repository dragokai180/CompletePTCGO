from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d6baa4c-bd56-5fa1-8259-76c8d1d81764',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name',
    display_name='Chimchar',
    searchable_by=['Chimchar', 'Basic', 'Chimchar'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=390,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Ember',
            game_text='Flip a coin. If tails, discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
