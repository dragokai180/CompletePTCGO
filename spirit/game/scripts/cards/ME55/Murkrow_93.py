from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4da97380-686a-5e7f-9e26-6b30c738e334',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    display_name='Murkrow',
    searchable_by=['Murkrow', 'Basic', 'Murkrow'],
    subtypes=['Basic'],
    collector_number=93,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=198,
    abilities=[
        Attack(
            title='Clumsily Clutch',
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
