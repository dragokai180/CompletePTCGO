from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='113e6658-3259-54c9-ba3f-bfc6fccb5892',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name',
    display_name='Pidgey',
    searchable_by=['Pidgey', 'Basic', 'Pidgey'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=16,
    abilities=[
        Attack(
            title='Messenger',
            game_text='Search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle Pidgey and all cards attached to it back into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
