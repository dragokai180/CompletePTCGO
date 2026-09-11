from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b96fda8c-1878-5df2-ad19-0c11f0727fb0',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name',
    display_name='Klefki',
    searchable_by=['Klefki', 'Basic', 'Klefki'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dull Light',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
