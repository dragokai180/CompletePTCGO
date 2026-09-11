from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b4a1275-bc5b-5b76-9929-ebdac0110cd1',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name',
    display_name='Kricketot',
    searchable_by=['Kricketot', 'Basic', 'Kricketot'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=401,
    abilities=[
        Attack(
            title='Bug Hunch',
            game_text='Search your deck for up to 3 Grass Pokémon, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
