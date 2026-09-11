from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='888d3561-fa85-5e22-8fcb-2aefeb017b96',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    display_name='Zubat',
    searchable_by=['Zubat', 'Basic', 'Zubat'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=41,
    abilities=[
        Ability(
            title='Revealing Echo',
            game_text='Once during your turn, if this Pokémon is in the Active Spot, you may have your opponent reveal their hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
