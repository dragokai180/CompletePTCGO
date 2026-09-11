from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a82052b-5b4b-58e2-bb15-a333e11a557f',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name',
    display_name='Dunsparce',
    searchable_by=['Dunsparce', 'Basic', 'Dunsparce'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=206,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
