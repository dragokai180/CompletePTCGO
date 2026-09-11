from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='358eedf0-3098-564b-97df-18cea3744e66',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name',
    display_name='Meltan',
    searchable_by=['Meltan', 'Basic', 'Meltan'],
    subtypes=['Basic'],
    collector_number=128,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=808,
    abilities=[
        Attack(
            title='Steel Melt',
            game_text="If your opponent's Active Pokémon is a Metal Pokémon, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
