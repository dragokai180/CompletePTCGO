from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a5b3a57-2d2c-5beb-88de-4c62a9aafa14',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    display_name='Honedge',
    searchable_by=['Honedge', 'Basic', 'Honedge'],
    subtypes=['Basic'],
    collector_number=92,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Attack(
            title='Lucky Find',
            game_text='Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pierce',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
