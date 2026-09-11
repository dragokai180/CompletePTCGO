from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f054aa4c-ecb4-5178-b83e-23c5d19a5504',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    display_name='Clefairy',
    searchable_by=['Clefairy', 'Basic', 'Clefairy'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=35,
    abilities=[
        Attack(
            title='Minimize',
            game_text="During your opponent's next turn ,any damage done to Clefairy by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
