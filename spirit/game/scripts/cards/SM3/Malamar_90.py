from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4328d7ba-97a8-5088-94ae-602c6ae9a038',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name',
    display_name='Malamar',
    searchable_by=['Malamar', 'Stage 1', 'Malamar'],
    subtypes=['Stage 1'],
    collector_number=90,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name',
    family_id=686,
    abilities=[
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Energy Slosh',
            game_text='You may move all Energy attached to this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
