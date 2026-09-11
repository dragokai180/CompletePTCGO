from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd1ff823-3850-5f79-82fe-0c55fcfc31d0',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name',
    display_name='Alolan Rattata',
    searchable_by=['Alolan Rattata', 'Basic', 'AlolanRattata'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=19,
    abilities=[
        Attack(
            title='Call for the Boss',
            game_text='Search your deck for Alolan Raticate or Alolan Raticate-GX, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
