from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b3084b64-8667-5baf-a7ea-06b2ab111377',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name',
    display_name='Ralts',
    searchable_by=['Ralts', 'Basic', 'Ralts'],
    subtypes=['Basic'],
    collector_number=139,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=280,
    abilities=[
        Attack(
            title='Beckon',
            game_text='Put a Supporter card from your discard pile into your hand.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
