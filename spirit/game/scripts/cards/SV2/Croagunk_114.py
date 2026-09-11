from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e00c1e3b-8ea7-505d-9e3b-4287f1ae2eb7',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    display_name='Croagunk',
    searchable_by=['Croagunk', 'Basic', 'Croagunk'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=453,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
