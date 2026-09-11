from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f000419d-c160-5bc9-814a-3e6f84ef91a8',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name',
    display_name='Lechonk',
    searchable_by=['Lechonk', 'Basic', 'Lechonk'],
    subtypes=['Basic'],
    collector_number=181,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=915,
    abilities=[
        Attack(
            title='Disarming Voice',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
