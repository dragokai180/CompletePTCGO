from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b4b5492e-5a85-596e-a73b-f59989cb4ea2',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    display_name='Flabébé',
    searchable_by=['Flabébé', 'Basic', 'Flabb'],
    subtypes=['Basic'],
    collector_number=149,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Attack(
            title='Floral Invitation',
            game_text='Search your deck for up to 2 Fairy Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
