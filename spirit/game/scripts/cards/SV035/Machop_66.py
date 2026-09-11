from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1926d48d-216e-5d5a-97cf-b4e81ef70be7',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    display_name='Machop',
    searchable_by=['Machop', 'Basic', 'Machop'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=66,
    abilities=[
        Attack(
            title='Mountain Mashing',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Punch',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
