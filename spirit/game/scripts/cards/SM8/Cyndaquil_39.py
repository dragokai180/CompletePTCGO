from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1be770a5-8d06-587d-80ed-0d7b953c1856',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name',
    display_name='Cyndaquil',
    searchable_by=['Cyndaquil', 'Basic', 'Cyndaquil'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=155,
    abilities=[
        Attack(
            title='Smokescreen',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
