from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='930e779c-b248-504f-b6de-56a5a5788b34',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    display_name='Clefairy',
    searchable_by=['Clefairy', 'Basic', 'Clefairy'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=35,
    abilities=[
        Attack(
            title='Moon-Viewing Invitation',
            game_text='Search your deck for up to 3 Clefairy and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Smack',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
