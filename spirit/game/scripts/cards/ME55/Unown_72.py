from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='946cfca0-8f41-53cb-87db-2aefcb621428',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name',
    display_name='Unown',
    searchable_by=['Unown', 'Basic', 'Unown'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=201,
    abilities=[
        Attack(
            title='Mysterious Signal',
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
