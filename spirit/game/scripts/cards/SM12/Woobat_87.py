from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ebcc569-1f9c-5ac5-b107-6d529bbcc8e7',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name',
    display_name='Woobat',
    searchable_by=['Woobat', 'Basic', 'Woobat'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=527,
    abilities=[
        Attack(
            title='Nasal Suction',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Air Cutter',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
