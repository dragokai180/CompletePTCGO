from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7bb6fe87-a613-55f7-909d-e24def8def25',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name',
    display_name='Wattrel',
    searchable_by=['Wattrel', 'Basic', 'Wattrel'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=940,
    abilities=[
        Attack(
            title='Devastating Wind',
            game_text='Your opponent shuffles their hand into their deck and draws 4 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
